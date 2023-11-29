#include "lists.h"

/**
 * createNode - adds a new node at the end of a listint_t list
 * @data: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */

listint_t* createNode(int data)
		{
    listint_t* newNode = (listint_t*)malloc(sizeof(listint_t));

    if (newNode == NULL)
    {
        perror("Error creating a new node");
        exit(EXIT_FAILURE);
    }
    newNode->data = data;
    newNode->next = NULL;
    return (newNode);
}

/**
 * insert_node - inserts data in a sorted list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */


listint_t* insert_node(listint_t** head, int number)
{
    listint_t* newNode = createNode(number);

    if (*head == NULL || number < (*head)->data)
    {
        newNode->next = *head;
        *head = newNode;
        return (newNode);
    }

    listint_t* current = *head;

    while (current->next != NULL && current->next->data < number)
    {
        current = current->next;
    }

    newNode->next = current->next;
    current->next = newNode;

    return (newNode);  
}
