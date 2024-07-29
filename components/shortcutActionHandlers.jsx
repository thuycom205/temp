import {approveProgram, handleJoinProgram} from './entityActionHandlers';

// Dynamic action handlers map
const dynamicActionHandlers = {
    joinProgram: handleJoinProgram,
    approve:approveProgram
    // Add other dynamic action handlers here
};

const getDynamicActions = (id,item, actions) => actions.map(action => ({
    content: action.label,
    onAction: () => {
        const actionHandler = dynamicActionHandlers[action.actionType];
        if (actionHandler) {
            actionHandler(id,item);
        } else {
            console.warn(`No handler defined for action type: ${action.actionType}`);
        }
    },
}));

const defaultShortcutActions = (item, actionHandlers) => [

    {
        content: 'Edit',
        onAction: () => actionHandlers.handleEdit(item.id),
    },
    // Default actions...
];

const questionShortcutActions = (item, actionHandlers) => [
    // Entity-specific actions...
];

export const getShortcutActions = (id,entity, item, actionHandlers, schemaActions) => {
    // Check if dynamic actions are defined in the schema
    if (schemaActions && schemaActions.length > 0) {
        return getDynamicActions(id,item, schemaActions);
    }

    // Fallback to default or entity-specific actions if no dynamic actions are defined
    switch (entity) {
        case 'question':
            return questionShortcutActions(item, actionHandlers);
        default:
            return defaultShortcutActions(item, actionHandlers);
    }
};
