#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a node in a sorted linked list
 * @head: head of the list
 * @number: number of the node
 *
 * Return: pointer to the newly created node, if the function fails to insert
 * the node, it will return NULL.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *previous = NULL;
	listint_t *node = malloc(sizeof(listint_t));
	if (node == NULL)
	{
		free(node);
		return (NULL);
	}
	node->n = number;

	if (!*head)
	{
		*head = node;
		return (*head);
	}

	for(;;) {
		if (current->n >= number)
		{
			node->next = current;
			if (previous != NULL)
				previous->next = node;
			if (current == *head)
				*head = node;
			return (node);
		}
		previous = current;
		current = current->next;
		if (!current)
		{
			previous->next = node;
			return (node);
		}
	} 
}
