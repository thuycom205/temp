import React, { useReducer, useState, useEffect } from 'react';
import { AppProvider, Page, Layout, Card, Button, Stack, Select } from '@shopify/polaris';
import { PauseMajor, PlusMinor, DeleteMinor } from '@shopify/polaris-icons';
import ConditionGroup from './ConditionGroup';
import LogicalExpression from './LogicalExpression';
import { initialState, reducer } from './reducer';

const ActionCard = ({ ruleId, shopName }) => {
    const [state, dispatch] = useReducer(reducer, initialState);
    const [activeGroupId, setActiveGroupId] = useState(null);
    const [loading, setLoading] = useState(true);
    const [currentRuleId, setCurrentRuleId] = useState(ruleId);

    useEffect(() => {
        if (ruleId > 0 ) {
            fetch(`/api/rules/${ruleId}/conditions?shopName=${shopName}`)
                .then((response) => response.json())
                .then((data) => {
                    if (data.success) {
                        const conditions = JSON.parse(data.conditions);
                        const fetchedState = {
                            ...initialState,
                            groups: conditions, // Use the conditions key from the response
                        };
                        dispatch({type: 'INIT_STATE', payload: fetchedState});
                    } else {
                        console.error('Failed to fetch conditions:', data.message);
                    }
                    setLoading(false);
                })
                .catch((error) => {
                    console.error('Error fetching conditions:', error);
                    setLoading(false);
                });
        }
        }, [currentRuleId, shopName]);

    const handleConditionChange = (groupId, id, field, value) => {
        dispatch({
            type: 'UPDATE_CONDITION',
            payload: { groupId, id, field, value },
        });
    };

    const handleAddCondition = (groupId) => {
        dispatch({
            type: 'ADD_CONDITION',
            payload: { groupId },
        });
        setActiveGroupId(groupId);
    };

    const handleAddGroup = (groupId) => {
        dispatch({
            type: 'ADD_GROUP',
            payload: { groupId },
        });
        setActiveGroupId(groupId);
    };

    const handleAddSiblingGroup = () => {
        dispatch({
            type: 'ADD_SIBLING_GROUP',
        });
        setActiveGroupId(null);
    };

    const handleRemoveCondition = (groupId, conditionId) => {
        console.log('Dispatching REMOVE_CONDITION with', { groupId, conditionId });
        dispatch({
            type: 'REMOVE_CONDITION',
            payload: { groupId, conditionId },
        });
    };

    const handleSubmit = () => {
        fetch(`/api/rules/${currentRuleId}/conditions`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                conditions: state.groups,
                shop_name: shopName,
                rule_name: 'Your Rule Name', // Replace with the actual rule name if available
                action: 'Your Action', // Replace with the actual action if available
            }),
        })
            .then((response) => response.json())
            .then((data) => {
                if (data.success) {
                    console.log('Conditions saved successfully');
                    if (currentRuleId === 0) {
                        setCurrentRuleId(data.rule_id);
                    }
                } else {
                    console.error('Failed to save conditions');
                }
            });
    };

    if (loading) {
        return <div>Loading...</div>;
    }

    return (
        <Layout>
            <Layout.Section>
                <Card sectioned>
                    <Stack vertical>
                        <Button icon={PauseMajor} plain>
                            Pause Campaign
                        </Button>
                        {state.groups.map((group, index) => (
                            <div key={group.id}>
                                {index > 0 && (
                                    <Select
                                        options={[
                                            { label: 'AND', value: 'AND' },
                                            { label: 'OR', value: 'OR' },
                                        ]}
                                        value={group.connector}
                                        onChange={(value) => handleConditionChange(null, group.id, 'connector', value)}
                                    />
                                )}
                                <ConditionGroup
                                    group={group}
                                    onChange={handleConditionChange}
                                    onRemove={handleRemoveCondition}
                                    onAddCondition={handleAddCondition}
                                    onAddGroup={handleAddGroup}
                                    parentLabel={`Group ${group.id}`}
                                    activeGroupId={activeGroupId}
                                />
                            </div>
                        ))}
                        <Button icon={PlusMinor} onClick={handleAddSiblingGroup}>
                            Add Sibling Group
                        </Button>
                        <Button onClick={handleSubmit}>Save Conditions</Button>
                    </Stack>
                </Card>
            </Layout.Section>
            <Layout.Section secondary>
                <LogicalExpression groups={state.groups} />
            </Layout.Section>
        </Layout>
    );
};

export default ActionCard;
