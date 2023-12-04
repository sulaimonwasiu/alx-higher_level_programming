#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is _palindrome - check for symmetry
 * @head: head of the list
 *
 * Return: an integer
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *prev = NULL, *next;

	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (1);

	while (fast && fast->next)
	{
		fast = fast->next->next;
		next = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next;
	}

	if (fast)
		slow = slow->next;
	while (slow)
	{
		if (slow->n != prev->n)
			return (0);
		slow = slow->next;
		prev = prev->next;
	}

	return (1);
}
