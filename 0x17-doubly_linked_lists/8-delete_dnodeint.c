
#include "lists.h"  
/**
 * delete_dnodeint_at_index - Deletes the node at a given index of a doubly linked list.
 * @head: A pointer to the address of the head of the list.
 * @index: The index of the node that should be deleted, starting from 0.
 *
 * Return: 1 if the deletion succeeded, -1 if it failed.
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	dlistint_t *current = *head;

	if (head == NULL || *head == NULL)
		return (-1);

	if (index == 0)
	{
		*head = current->next;
		if (current->next != NULL)
			current->next->prev = NULL;
		free(current);
		return (1);
	}

	while (current != NULL && index > 0)
	{
		current = current->next;
		index--;
	}

	if (current == NULL)
		return (-1);

	current->prev->next = current->next;

	if (current->next != NULL)
		current->next->prev = current->prev;

	free(current);

	return (1);
}
