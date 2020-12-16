#include "lists.h"
/**
 * is_palindrome - Function checks if a singly linked list is a palindrome
 * @head: pointer to the singly linked list
 *
 * Return: 0 if not a palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *end, *curr;
	int end_i = 0, index = 0, length = 0;

	if (head == NULL || (*head) == NULL)
		return (1);
	curr = (*head);
	/*Find the length*/
	while (curr != NULL)
	{
		length++;
		curr = curr->next;
	}
	curr = (*head);
	while (index < (length / 2))
	{
		end_i = 0;
		end = curr;
		while (end_i < ((length - 1) - (index * 2)))
		{
			end = end->next;
			end_i++;
		}
		if (end->n != curr->n)
		{
			return (0);
		}
		curr = curr->next;
		index++;
	}
	return (1);
}
