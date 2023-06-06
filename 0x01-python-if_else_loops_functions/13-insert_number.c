
#include "lists.h"

listint_t* insert_node(listint_t** head, int number)
{
	listint_t* new_node = (listint_t*)malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		return (NULL);
	}
	new_node->data = number;
	new_node->next = NULL;

	if (*head == NULL || number < (*head)->data)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	listint_t* current = *head;

	while (current->next != NULL && current->next->data < number)
	{
		current = current->next;
	}

	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}
