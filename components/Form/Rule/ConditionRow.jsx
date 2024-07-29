import React from 'react';
import { Stack, Select, TextField, Button } from '@shopify/polaris';
import { DeleteMinor } from '@shopify/polaris-icons';

const ConditionRow = ({ condition, groupId, onChange, onRemove }) => (
    <Stack alignment="center" spacing="tight">
        <Select
            options={[
                { label: 'Campaign • Ad Spend', value: 'Campaign • Ad Spend' },
                { label: 'Campaign • Purchase', value: 'Campaign • Purchase' },
                { label: 'Campaign • Cost per Purchase', value: 'Campaign • Cost per Purchase' },
            ]}
            value={condition.field}
            onChange={(value) => onChange(groupId, condition.id, 'field', value)}
        />
        <Select
            options={[
                { label: 'Today', value: 'Today' },
                { label: 'Yesterday', value: 'Yesterday' },
                { label: 'Today and Yesterday', value: 'Today and Yesterday' },
                { label: 'Last 2 days', value: 'Last 2 days' },
                { label: 'Last 3 days', value: 'Last 3 days' },
                { label: 'Last 7 days', value: 'Last 7 days' },
                { label: 'Last 14 days', value: 'Last 14 days' },
                { label: 'Last 30 days', value: 'Last 30 days' },
                { label: 'Last 2 days (including today)', value: 'Last 2 days (including today)' },
                { label: 'Last 3 days (including today)', value: 'Last 3 days (including today)' },
                { label: 'Last 7 days (including today)', value: 'Last 7 days (including today)' },
                { label: 'Last 14 days (including today)', value: 'Last 14 days (including today)' },
                { label: 'Last 30 days (including today)', value: 'Last 30 days (including today)' },
                { label: 'Lifetime', value: 'Lifetime' },
            ]}
            value={condition.timeframe}
            onChange={(value) => onChange(groupId, condition.id, 'timeframe', value)}
        />
        <Select
            options={[
                { label: 'is greater than', value: 'is greater than' },
                { label: 'is equal', value: 'is equal' },
                { label: 'is less than or equal', value: 'is less than or equal' },
                { label: 'is greater than or equal', value: 'is greater than or equal' },
            ]}
            value={condition.operator}
            onChange={(value) => onChange(groupId, condition.id, 'operator', value)}
        />
        <TextField
            value={condition.value}
            onChange={(value) => onChange(groupId, condition.id, 'value', value)}
            type="number"
        />
        {condition.unit && (
            <Select
                options={[
                    { label: 'USD', value: 'USD' },
                ]}
                value={condition.unit}
                onChange={(value) => onChange(groupId, condition.id, 'unit', value)}
            />
        )}
        <Button icon={DeleteMinor} onClick={() => onRemove(groupId, condition.id)} />
    </Stack>
);

export default ConditionRow;
