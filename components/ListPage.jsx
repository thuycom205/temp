import React, { useState, useCallback, useEffect } from 'react';
import {
    Page,
    Button,
    ResourceList,
    Card,
    ResourceItem,
    TextStyle,
    Stack,
    Pagination,
    EmptyState,
    Frame,
    Toast,
} from '@shopify/polaris';
import { QuestionMarkMajor,QuestionMarkMinor } from '@shopify/polaris-icons';
import { Tooltip, Icon } from '@shopify/polaris';

// import { useNavigate } from "@shopify/app-bridge-react";
import { useLocation, useNavigate } from "react-router-dom";
import {useShop} from "../providers/ShopProvider";
import { getEntityActionHandlers } from './entityActionHandlers';
import { getShortcutActions } from './shortcutActionHandlers';
import { getBulkActions } from './bulkActionsRegistry';  // Updated import
import { Spinner } from '@shopify/polaris'; // Import Spinner for loading indicator

function useForceUpdate() {
    const [, setTick] = useState(0);
    const update = useCallback(() => {
        setTick(tick => tick + 1);
    }, []);
    return update;
}
const ListPage = ({ title, resourceName, fetchUrl, deleteUrl, createUrl, editUrl, itemsPerPage = 50 ,entity ,schema}) => {
    const forceUpdate = useForceUpdate();

    const location = useLocation();
    const query = new URLSearchParams(location.search);
    const editId = query.get('id'); // Assuming the URL parameter name is 'id'

    const {shopxName, apiKeyx, token, listIdx } = useShop();
    const  navigate = useNavigate();
    // Improved logic to use shopxName or fall back to localStorage
    const initialShop = shopxName || localStorage.getItem('shop') || '';
    const [shop, setShop] = useState(initialShop);
    const actionHandlers = getEntityActionHandlers(entity, navigate, shop, token);

    const [items, setItems] = useState([]);
    const [selectedItems, setSelectedItems] = useState([]);

    const [currentPage, setCurrentPage] = useState(1);
    const [totalItemCount, setTotalItemCount] = useState(0);
    const [assignMapId, setAssignMapId] = useState(null);

    const [toastActive, setToastActive] = useState(false);
    const [toastMessage, setToastMessage] = useState('');
    const [toastError, setToastError] = useState(false);
    const [bulkActions, setBulkActions] = useState([]);
    const [isLoading, setIsLoading] = useState(false); // State to track loading

    useEffect(() => {
        const handleDeleteSelected = async () => {
            console.log('Selected items to delete:', selectedItems);
            try {
                const response = await fetch(deleteUrl, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ ids: selectedItems, shop_name: shop }),
                });
                if (!response.ok) throw new Error('Network response was not ok.');
                const data = await response.json();
                setToastMessage(data.message || 'Items deleted successfully.');
                setToastActive(true);
                const remainingItems = items.filter(item => !selectedItems.includes(item.id.toString()));
                setItems(remainingItems);
            } catch (error) {
                console.error('Error:', error);
                setToastMessage('Failed to delete items.');
                setToastActive(true);
            }
        };

        setBulkActions([
            {
                content: 'Delete',
                onAction: handleDeleteSelected,
            },
            // Load other dynamic actions as needed
        ]);
    }, [deleteUrl, selectedItems, shop, items]);


    // useEffect(() => {
    //     const loadBulkActions = async () => {
    //         try {
    //             const actionsModule = await import(`./bulkActions/${entity}Actions`);
    //             const entityBulkActions = actionsModule.getBulkActions(selectedItems, setItems, navigate, items);
    //             // Ensure the default Delete action is always included
    //             setBulkActions(previousActions => [
    //                 ...previousActions.filter(action => action.content === 'Delete'),
    //                 ...entityBulkActions
    //             ]);
    //         } catch (error) {
    //             console.error(`Failed to load bulk actions for entity ${entity}:`, error);
    //         }
    //     };
    //
    //     loadBulkActions();
    // }, [entity, selectedItems, setItems, navigate]);

    useEffect(() => {
        // Define default actions that apply to all entities
        const defaultBulkActions = [
            {
                content: 'Delete',
                onAction: async () => {
                    console.log('Deleting selected items:', selectedItems);
                    try {
                        const response = await fetch(deleteUrl, {
                            method: 'POST',
                            headers: { 'Content-Type': 'application/json' },
                            body: JSON.stringify({ ids: selectedItems,shop_name:shop })
                        });
                        if (!response.ok) throw new Error('Failed to delete items.');

                        // Update the UI to reflect the deletion
                        setItems(prevItems => prevItems.filter(item => !selectedItems.includes(item.id)));

                        setSelectedItems([]);
                        alert('Items deleted successfully.');
                    } catch (error) {
                        console.error('Error deleting items:', error);
                        alert('Failed to delete items.');
                    }
                }
            }
        ];

        // Get entity-specific actions
        // const entitySpecificActions = getBulkActions(entity).map(action => ({
        //     content: action.content,
        //     onAction: () => action.handler(selectedItems, setItems, items)
        // }));
        const entitySpecificActions = getBulkActions(entity).map(action => ({
            content: action.content,
            helpText: action.helpText? action.helpText: '',
            onAction: () => {
                action.handler(selectedItems, setItems, items,setSelectedItems, setIsLoading);
                forceUpdate(); // This forces the component to re-render after the action
            }
        }));
        // Combine default and entity-specific actions
        const combinedBulkActions = [...defaultBulkActions, ...entitySpecificActions];
        setBulkActions(combinedBulkActions);

        // Any other setup logic for page load
    }, [entity, selectedItems, items, deleteUrl]);


    const toggleActive = useCallback(() => setToastActive((active) => !active), []);
    const toastMarkup = toastActive ? (
        <Toast content={toastMessage} onDismiss={toggleActive} error={toastError} />
    ) : null;
    const handleNextPage = useCallback(() => {
        setCurrentPage(currentPage + 1);
    }, [currentPage]);
    const toggleToastActive = useCallback(() => {
        setToastActive((active) => !active);
    }, []);

    const renderAdditionalFields = (item) => {
        // Assuming schema.tree.fields exists and is an array
        return schema.tree.fields.map((field) => {
            switch (field.type) {
                case 'text':
                    return <div key={field.name}>{field.label}: {item[field.name]}</div>;
                // You can handle other types (e.g., 'select') similarly
                default:
                    return null;
            }
        });
    };

    const handlePreviousPage = useCallback(() => {
        setCurrentPage(currentPage - 1);
    }, [currentPage]);

    const handleSelectionChange = useCallback((items) => {
        setSelectedItems(items);
    }, []);
    useEffect(() => {
        const fetchData = async () => {
           // alert(shop);
            setIsLoading(true); // Start loading

            const params = {
                shop_name: shop,
                page: currentPage,
                items_per_page: itemsPerPage,
            };

            try {
                const response = await fetch(fetchUrl, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(params),
                });

                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }

                const data = await response.json();
                setItems(data.items);
                setTotalItemCount(data.totalItemCount);
            } catch (error) {
                console.error('Failed to fetch items:', error);
            } finally {
                setIsLoading(false); // End loading
            }
        };
        const fetchDataLiveOrder = async () => {
            // alert(shop);
            setIsLoading(true); // Start loading

            const params = {
                shop_name: shop
            };

            try {
                const fetChLiveOrder =`/api/af_kol/fetchOrder`;

                const response = await fetch(fetChLiveOrder, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(params),
                });

                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }

                const data = await response.json();

            } catch (error) {
                console.error('Failed to fetch items:', error);
            } finally {
                setIsLoading(false); // End loading
            }
        };
        fetchData();

        if (entity === 'affiliate_order') {
            fetchDataLiveOrder();
        }
    }, [currentPage, itemsPerPage, fetchUrl,location]);

    const handleCreateNew = useCallback(() => {
        // Use the createUrl to navigate to the creation page
        navigate(createUrl +`?editId=${0}`);
    }, [createUrl]);

    const handleEdit = useCallback((id) => {
        // Use the editUrl to navigate to the edit page
        navigate(editUrl + `?editId=${id}` + `&shop_name=${shop}`) ;

    }, [editUrl]);

    const handleAssignProduct =useCallback((id,name) => {
        console.log(id);
        setAssignMapId(id);
        window.assign_map_id = id;
        window.assign_map_name = name;
        console.log(assignMapId);
        // Use the editUrl to navigate to the edit page
        navigate('/page_seat_assign_product' + `?editId=${id}` + `&shop_name=${shop}`) ;
    },[assignMapId]);



    const handleAssignProducts = useCallback(async () => {
        console.log(selectedItems);

    },[ selectedItems]);

    // ... other handlers ...

    // const renderContent = () => {
    //     if (items.length === 0 && totalItemCount === 0) {
    //         return (
    //             <EmptyState
    //                 heading={`No ${resourceName.plural.toLowerCase()} found`}
    //                 action={{
    //                     content: `Create ${resourceName.singular}`,
    //                     onAction: handleCreateNew,
    //                 }}
    //             >
    //                 <p>Click the button to start creating a new item.</p>
    //             </EmptyState>
    //         );
    //     } else {
    //         return (
    //             <ResourceList
    //                 resourceName={resourceName}
    //                 items={items}
    //                 selectedItems={selectedItems}
    //                 onSelectionChange={handleSelectionChange}
    //                 bulkActions={bulkActions}
    //
    //                 renderItem={(item) => {
    //                     const { id, title } = item;
    //
    //                     // const shortcutActions = getShortcutActions(entity, item, {
    //                     //     handleAssignProduct: handleAssignProduct,
    //                     //     handleEdit: handleEdit,
    //                     //     // Add other handlers here as needed
    //                     //     handleShowQuiz: (id) => {
    //                     //         console.log("Showing quiz for question ID:", id);
    //                     //         // Implement the logic to show the quiz here
    //                     //     },
    //                     // });
    //                     const shortcutActions = getShortcutActions(editId,entity, item, actionHandlers, schema.tree.actions);
    //
    //                     return (
    //                         <ResourceItem
    //                             id={id.toString()}
    //                             accessibilityLabel={`Edit ${title}`}
    //                             name={title}
    //                             persistActions
    //                             shortcutActions={shortcutActions}
    //
    //                             // shortcutActions={[
    //                             //
    //                             //     { content: 'Edit', onAction:() => {
    //                             //     actionHandlers.handleEdit(id)      }
    //                             //     }
    //                             // ]}
    //                         >
    //                             {/*<TextStyle variation="strong">{title}</TextStyle>*/}
    //                             {renderAdditionalFields(item)}
    //
    //                         </ResourceItem>
    //                     );
    //                 }}
    //             />
    //         );
    //     }
    // };

    const renderContent = useCallback(() => {
        if (items.length === 0 && totalItemCount === 0) {
            return (
                <EmptyState
                    heading={`No ${resourceName.plural.toLowerCase()} found`}
                    action={{
                        content: `Create ${resourceName.singular}`,
                        onAction: handleCreateNew,
                    }}
                >
                    <p>Click the button to start creating a new item.</p>
                </EmptyState>
            );
        } else {
            return (
                <ResourceList
                    resourceName={resourceName}
                    items={items}
                    selectedItems={selectedItems}
                    onSelectionChange={handleSelectionChange}
                    bulkActions={bulkActions}
                    renderItem={(item) => {
                        const { id, title } = item;
                        const shortcutActions = getShortcutActions(editId, entity, item, actionHandlers, schema.tree.actions);

                        return (
                            <ResourceItem
                                id={id.toString()}
                                accessibilityLabel={`Edit ${title}`}
                                name={title}
                                persistActions
                                shortcutActions={shortcutActions}
                            >
                                {renderAdditionalFields(item)}
                            </ResourceItem>
                        );
                    }}
                />
            );
        }
    }, [items, resourceName, selectedItems, bulkActions, totalItemCount, handleCreateNew, handleSelectionChange, editId, entity, actionHandlers, schema.tree.actions]);
    if (isLoading) {
        console.log('is loading');
        return <Spinner accessibilityLabel="Loading items" size="large" />;
    }

    const helpText= schema.tree.helpText?schema.tree.helpText:`Showing ${items.length} of ${totalItemCount} ${resourceName.plural.toLowerCase()}`;
    return (
            <Page
                title={title}
                primaryAction={{
                    content: `Create ${resourceName.singular}`,
                    onAction: handleCreateNew,
                }}
                helpText={helpText}
            >
                <Stack alignment="center" spacing="tight">
                    <span style={{ marginRight: '8px' }}>Help</span>
                    <Tooltip content={helpText} dismissOnMouseOut>
                        <div style={{ display: 'inline-block', lineHeight: 0, verticalAlign: 'middle' }}>
                            <Icon source={QuestionMarkMinor} color="highlight" />
                        </div>
                    </Tooltip>
                </Stack>
                <Card sectioned>
                    {renderContent()}
                </Card>
                {toastMarkup}
                  <Stack distribution="trailing">
                        <Pagination
                            hasPrevious={currentPage > 1}
                            onPrevious={handlePreviousPage}
                            hasNext={currentPage * itemsPerPage < totalItemCount}
                            onNext={handleNextPage}
                        />
                  </Stack>
            </Page>
    );
};

export default ListPage;
