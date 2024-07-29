import React from 'react';
import { Card, TextStyle } from '@shopify/polaris';

const LogicalExpression = ({ groups }) => {
    const renderGroup = (group) => {
        const conditions = group.conditions.map((cond) => `${cond.field} ${cond.operator} ${cond.value} ${cond.unit}`).join(` ${group.connector} `);
        const subGroups = group.groups.map((subGroup) => renderGroup(subGroup)).join(` ${group.connector} `);

        return `(${conditions}${conditions && subGroups ? ` ${group.connector} ` : ''}${subGroups})`;
    };

    return (
        <Card sectioned title="Logical Expression">
            <TextStyle variation="code">{groups.map((group) => renderGroup(group)).join(' AND ')}</TextStyle>
        </Card>
    );
};

export default LogicalExpression;
