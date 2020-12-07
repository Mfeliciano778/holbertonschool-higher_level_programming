#include "lists.h"
/**
 * check_cycle - check if linked list is a cycle
 * @list: head of the linked list
 *
 * Return: 1 if cycle; 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_pt = list, *fst_pt = list;

	while (slow_pt && fst_pt && fst_pt->next)
	{
		slow_pt = slow_pt->next;
		fst_pt = fst_pt->next->next;
		if (slow_pt == fst_pt)
		{
			return (1);
		}
	}
	return (0);
}
