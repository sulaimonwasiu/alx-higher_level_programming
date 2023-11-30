#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

listint_t *create_node(int data);

/**
 * insert_node - prints all elements of a listint_t list
 * @head: pointer to head of list
 * @number: data
 * Return: inserted node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = create_node(number);
	listint_t *current = *head;

	if (*head == NULL || number < (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	while (current->next != NULL && current->next->n < number)
	{
		current = current->next;
	}
	new->next = current->next;
	current->next = new;
	return (new);
}
