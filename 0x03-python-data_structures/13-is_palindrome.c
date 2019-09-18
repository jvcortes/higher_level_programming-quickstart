#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a listint_t linked list is a palindrome
 * @head: list head
 *
 * Return: if the list is a palindrome, the function will return 1, else, 0.
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int *n;
	int i = 0, j = 0, palindrome = 1;

	if (!*head)
		return (1);

	while (current)
	{
		current = current->next;
		i++;
	}
	current = *head;

	n = malloc(sizeof(int) * i);
	i = 0;
	while (current)
	{
		n[i++] = current->n;
		current = current->next;
	}

	for (j = i - 1, i = 0; j >= 0; i++, j--)
		if (n[i] != n[j])
		{
			palindrome = 0;
			break;
		}

	free(n);
	return (palindrome);
}
