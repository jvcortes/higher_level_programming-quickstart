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
	listint_t *top = *head;
	listint_t *bottom = *head;
	int i = 0, j = 0;

	if (!*head)
		return (1);

	while (bottom->next)
	{
		bottom = bottom->next;
		i++;
	}

	i--;
	while (top)
	{
		j = 0;
		if (top->n != bottom->n)
			break;
		else if (bottom == *head)
			return (1);
		top = top->next;
		i--;
		bottom = *head;
		while (j <= i)
		{
			bottom = bottom->next;
			j++;
		}
	}

	return (0);
}
