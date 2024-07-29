import React, { useEffect, useRef ,useState} from 'react';
import 'selectize/dist/css/selectize.default.css';
import './selectize-custom.css'; // Import the custom CSS file
import $ from 'jquery';
import 'selectize';

const GoogleCategorySelectorWithSelectize = ({ label, value, onChange }) => {
    const selectRef = useRef(null);
    const [selectedValue, setSelectedValue] = useState(value);

    useEffect(() => {
        const $select = $(selectRef.current).selectize({
            valueField: 'name',
            labelField: 'name',
            searchField: 'name',
            create: false,
            placeholder: 'Search Google Categories',
            load: function(query, callback) {
                if (!query.length) return callback();
                fetch(`http://colab.ngrok.app/api/google-categories?search=${encodeURIComponent(query)}`)
                    .then(response => response.json())
                    .then(data => callback(data))
                    .catch(() => callback());
            },
            onChange: function(value) {
                console.log('Selected value:', value);
                setSelectedValue(value);

                onChange(value);


            }
        });

        // Set initial value
        const selectize = $select[0].selectize;
        selectize.setValue(value);

        return () => {
            selectize.destroy();
        };
    }, [onChange]);

    // Update Selectize when value changes
    useEffect(() => {
        const selectize = $(selectRef.current)[0].selectize;
        if (selectize) {
            console.log(selectize);
            selectize.setValue(value);
        }
    }, []);

    return (
        <div>
            <label>{label}</label>
            <select ref={selectRef}>
                <option value="">Search Google Categories</option>
            </select>
            {selectedValue && (
                <div style={{ marginTop: '10px' }}>
                    <strong>Selected Category:</strong> {selectedValue}
                </div>
            )}
        </div>
    );
};

export default GoogleCategorySelectorWithSelectize;
