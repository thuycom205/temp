import React, { useState, useEffect, useCallback } from 'react';
import { Select, Spinner, TextField, Stack } from '@shopify/polaris';

const GoogleCategorySelector = ({ label, value, onChange }) => {
    const [categories, setCategories] = useState([]);
    const [loading, setLoading] = useState(false);
    const [searchTerm, setSearchTerm] = useState('');

    useEffect(() => {
        if (searchTerm) {
            setLoading(true);
            fetch(`/api/google-categories?search=${encodeURIComponent(searchTerm)}`)
                .then(response => response.json())
                .then(data => {
                    setCategories(data);
                    setLoading(false);
                })
                .catch(error => {
                    console.error('Error fetching categories:', error);
                    setLoading(false);
                });
        }
    }, [searchTerm]);

    const handleSearchChange = useCallback((newValue) => {
        setSearchTerm(newValue);
    }, []);

    const handleSelectChange = useCallback((newValue) => {
        onChange(newValue);
    }, [onChange]);

    const options = categories.map(category => ({
        label: category.name,
        value: category.id.toString(),
    }));

    return (
        <div>
            <Stack vertical>
                <TextField
                    label={label}
                    value={searchTerm}
                    onChange={handleSearchChange}
                    placeholder="Type to search Google categories"
                />
                {loading ? (
                    <Spinner size="small" />
                ) : (
                    <Select
                        label="Select a Category"
                        options={options}
                        onChange={handleSelectChange}
                        value={value}
                        placeholder="Select a category"
                    />
                )}
            </Stack>
        </div>
    );
};

export default GoogleCategorySelector;
