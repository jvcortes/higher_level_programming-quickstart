#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a node in a sorted linked lists
 * @head: head of the list
 * @number: number of the node
 *
 * Return: pointer to the newly created node, if the function fails to insert
 * the node, it will return NULL.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *node;

	if (!*head)
	{
		*head = malloc(sizeof(listint_t));
		if (*head == NULL)
		{
			free(*head);
			return (NULL);
		}
		(*head)->n = number;
		return (*head);
	}

	do {
		if ((!current->next) || (current->n < number && current->next->n > number))
		{
			node = malloc(sizeof(listint_t));
			if (node == NULL)
			{
				free(node);
				return (NULL);
			}
			node->n = number;
			node->next = current->next;
			current->next = node;
			return (node);
		}
		current = current->next;

	} while (current->next);

	return (NULL);
}
