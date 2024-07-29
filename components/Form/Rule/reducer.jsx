const generateId = (() => {
    let id = 0;
    return () => ++id;
})();
const initialState = {
    id: 1,
    type: 'GROUP',
    connector: 'AND',
    conditions: [],
    groups: [],
};
// const initialState = {
//     id: generateId(),
//     type: 'GROUP',
//     connector: 'AND',
//     conditions: [],
//     groups: [
//         {
//             id: generateId(),
//             type: 'GROUP',
//             connector: 'AND',
//             conditions: [
//                 {
//                     id: generateId(),
//                     type: 'CONDITION',
//                     field: 'Campaign • Ad Spend',
//                     timeframe: 'Last 3 days (including today)',
//                     operator: 'is greater than',
//                     value: '75.00',
//                     unit: 'USD',
//                 },
//             ],
//             groups: [],
//         },
//         {
//             id: generateId(),
//             type: 'GROUP',
//             connector: 'AND',
//             conditions: [
//                 {
//                     id: generateId(),
//                     type: 'CONDITION',
//                     field: 'Campaign • Cost per Purchase',
//                     timeframe: 'Last 3 days (including today)',
//                     operator: 'is greater than',
//                     value: '20.00',
//                     unit: 'USD',
//                 },
//             ],
//             groups: [],
//         },
//     ],
// };

const reducer = (state, action) => {
    switch (action.type) {
        case 'INIT_STATE':
            return initState(action.payload);
        case 'ADD_CONDITION':
            return addCondition(state, action.payload.groupId);
        case 'UPDATE_CONDITION': {
            const { groupId, id, field, value } = action.payload;
            const condition = findCondition(state.groups, groupId, id);
            if (condition) {
                const updatedCondition = { ...condition, [field]: value };
                return updateCondition(state, updatedCondition);
            }
            return state;
        }
        case 'REMOVE_CONDITION':
            return removeCondition(state, action.payload.groupId, action.payload.conditionId);
        case 'ADD_GROUP':
            return addGroup(state, action.payload.groupId);
        case 'ADD_SIBLING_GROUP':
            return addSiblingGroup(state);
        case 'UPDATE_GROUP':
            return updateGroup(state, action.payload.group);
        case 'REMOVE_GROUP':
            return removeGroup(state, action.payload.groupId);
        default:
            return state;
    }
};

const initState = (fetchedState) => {
    const assignIds = (groups) => {
        return groups.map(group => ({
            ...group,
            id: generateId(),
            conditions: group.conditions.map(condition => ({
                ...condition,
                id: generateId()
            })),
            groups: assignIds(group.groups)
        }));
    };

    const stateWithIds = {
        ...fetchedState,
        groups: assignIds(fetchedState.groups)
    };

    return stateWithIds;
};

const addCondition = (state, groupId) => {
    const newCondition = {
        id: generateId(),
        type: 'CONDITION',
        field: 'Campaign • Ad Spend',
        timeframe: 'Last 3 days (including today)',
        operator: 'is greater than',
        value: '',
        unit: 'USD',
        connector: 'AND',
    };
    const addConditionToGroup = (groups) =>
        groups.map((group) =>
            group.id === groupId
                ? { ...group, conditions: [...group.conditions, newCondition] }
                : { ...group, groups: addConditionToGroup(group.groups) }
        );
    return {
        ...state,
        groups: addConditionToGroup(state.groups),
    };
};

// const updateCondition = (state, condition) => {
//     const updateConditionInGroup = (groups) =>
//         groups.map((group) => ({
//             ...group,
//             conditions: group.conditions.map((cond) => (cond.id === condition.id ? condition : cond)),
//             groups: updateConditionInGroup(group.groups),
//         }));
//     return {
//         ...state,
//         groups: updateConditionInGroup(state.groups),
//     };
// };
const findCondition = (groups, groupId, conditionId) => {
    for (let group of groups) {
        if (group.id === groupId) {
            for (let condition of group.conditions) {
                if (condition.id === conditionId) {
                    return condition;
                }
            }
        }
        const foundCondition = findCondition(group.groups, groupId, conditionId);
        if (foundCondition) {
            return foundCondition;
        }
    }
    return null;
};

const updateCondition = (state, condition) => {
    const updateConditionInGroup = (groups, condition) => {
        const updatedGroups = [];
        for (let group of groups) {
            console.log('Processing group:', group);

            // Create a copy of the group
            let updatedGroup = { ...group };

            // Update the conditions in the group
            const updatedConditions = [];
            for (let cond of group.conditions) {
                console.log('Checking condition:', cond);
                updatedConditions.push(cond.id === condition.id ? condition : cond);
            }
            updatedGroup.conditions = updatedConditions;

            // Recursively update the conditions in the sub-groups
            updatedGroup.groups = updateConditionInGroup(group.groups, condition);

            // Add the updated group to the updatedGroups array
            updatedGroups.push(updatedGroup);
        }
        return updatedGroups;
    };

    return {
        ...state,
        groups: updateConditionInGroup(state.groups, condition),
    };
};

const removeCondition = (state, groupId, conditionId) => {

    console.log('remove condtion', groupId, conditionId);
    const removeConditionFromGroup = (groups) =>
        groups.map((group) =>
            group.id === groupId
                ? { ...group, conditions: group.conditions.filter((condition) => condition.id !== conditionId) }
                : { ...group, groups: removeConditionFromGroup(group.groups) }
        );
    return {
        ...state,
        groups: removeConditionFromGroup(state.groups),
    };
};

const addGroup = (state, groupId) => {
    const newGroup = {
        id: generateId(),
        connector: 'AND',
        conditions: [],
        groups: [],
    };
    const addGroupToGroup = (groups) =>
        groups.map((group) =>
            group.id === groupId
                ? { ...group, groups: [...group.groups, newGroup] }
                : { ...group, groups: addGroupToGroup(group.groups) }
        );
    return {
        ...state,
        groups: addGroupToGroup(state.groups),
    };
};

const addSiblingGroup = (state) => {
    const newGroup = {
        id: generateId(),
        connector: 'AND',
        conditions: [],
        groups: [],
    };
    return {
        ...state,
        groups: [...state.groups, newGroup],
    };
};

const updateGroup = (state, group) => {
    const updateGroupInGroups = (groups) =>
        groups.map((grp) => (grp.id === group.id ? group : { ...grp, groups: updateGroupInGroups(grp.groups) }));
    return {
        ...state,
        groups: updateGroupInGroups(state.groups),
    };
};

const removeGroup = (state, groupId) => {
    console.log('remove group', groupId);
    const removeGroupFromGroups = (groups) =>
        groups.filter((group) => group.id !== groupId).map((group) => ({ ...group, groups: removeGroupFromGroups(group.groups) }));
    return {
        ...state,
        groups: removeGroupFromGroups(state.groups),
    };
};

export { initialState, reducer };
