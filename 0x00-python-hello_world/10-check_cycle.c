#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *slow = list;	
	listint_t *fast = list->next;

	while(slow != fast)
	{
		if (!fast->next || !fast->next->next)
			break;
		slow = slow->next;
		fast = fast->next->next;
	}

	if (slow == fast)
		return (1);
	else
		return (0);

}
