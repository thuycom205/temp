import React from 'react';
import { Card, Stack, Select, Button, TextStyle, Badge } from '@shopify/polaris';
import { PlusMinor } from '@shopify/polaris-icons';
import ConditionRow from './ConditionRow';

const ConditionGroup = ({
                            group,
                            onChange,
                            onRemove,
                            onAddCondition,
                            onAddGroup,
                            parentLabel,
                            activeGroupId,
                            level = 0,
                        }) => (
    <Card
        sectioned
        title={
            <Stack alignment="center">
                <Badge status="attention">{parentLabel}</Badge>
                {level > 0 && <TextStyle variation="subdued">Nested Group</TextStyle>}
            </Stack>
        }
        style={{
            borderColor: activeGroupId === group.id ? '#5c6ac4' : 'inherit',
            borderWidth: activeGroupId === group.id ? '2px' : '1px',
            borderStyle: 'solid',
            marginLeft: level * 20,
        }}
    >
        <Stack vertical>
            {group.conditions.map((condition, index) => (
                <div key={condition.id}>
                    {index > 0 && (
                        <Select
                            options={[
                                { label: 'AND', value: 'AND' },
                                { label: 'OR', value: 'OR' },
                            ]}
                            value={condition.connector}
                            onChange={(value) => onChange(group.id, condition.id, 'connector', value)}
                        />
                    )}
                    <ConditionRow
                        condition={condition}
                        groupId={group.id}
                        onChange={onChange}
                        onRemove={onRemove}
                    />
                </div>
            ))}
            {group.groups.map((subGroup, index) => (
                <div key={subGroup.id} style={{ marginLeft: 20 }}>
                    {index > 0 && (
                        <Select
                            options={[
                                { label: 'AND', value: 'AND' },
                                { label: 'OR', value: 'OR' },
                            ]}
                            value={subGroup.connector}
                            onChange={(value) => onChange(group.id, subGroup.id, 'connector', value)}
                        />
                    )}
                    <ConditionGroup
                        group={subGroup}
                        onChange={onChange}
                        onRemove={onRemove}
                        onAddCondition={onAddCondition}
                        onAddGroup={onAddGroup}
                        parentLabel={`${parentLabel} > Group ${subGroup.id}`}
                        activeGroupId={activeGroupId}
                        level={level + 1}
                    />
                </div>
            ))}
            <Stack distribution="equalSpacing">
                <Button icon={PlusMinor} onClick={() => onAddCondition(group.id)}>
                    Add Condition
                </Button>
                <Button icon={PlusMinor} onClick={() => onAddGroup(group.id)}>
                    Add Group
                </Button>
            </Stack>
        </Stack>
    </Card>
);

export default ConditionGroup;
