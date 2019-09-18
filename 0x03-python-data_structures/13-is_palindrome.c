#include <stdlib.h>
#include "lists.h"

#define SIZE 1024

/**
 * is_palindrome - checks if a listint_t linked list is a palindrome
 * @head: list head
 *
 * Return: if the list is a palindrome, the function will return 1, else, 0.
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int n[SIZE];
	int i = 0, j, size;

	if (!*head)
		return (1);

	i = 0;
	while (current)
	{
		n[i] = current->n;
		current = current->next;
		i++;
	}
	size = i;

	for (i = 0, j = size - 1; i < size && j >= 0; i++, j--)
		if (n[i] != n[j])
			return (0);

	return (1);
}
