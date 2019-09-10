#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle
 * @list: head of the list
 *
 * Return: if the linked list has a cycle, the function will return 1. Else
 * the function will return 0.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	do {
		if (!fast->next || !fast->next->next)
			break;
		slow = slow->next;
		fast = fast->next->next;
	} while (slow != fast);

	if (slow == fast)
		return (1);
	else
		return (0);

}
