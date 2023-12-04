#include "lists.h"
/**
 * reverse_listint - reverses a linked list
 * @head: pointer to the first node in the list
 *
 * Return: pointer to the first node in the new list
 */
void reverse_listint(listint_t **head)
{
	listint_t *prev = NULL, *next = NULL, *current = *head;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}
/**
 * is_palindrome - checks palindrome list
 * @head: the head of list
 * Return: an integer 0 or 1
*/
int is_palindrome(listint_t **head)
{
	listint_t *s = *head, *f = *head;
	listint_t *t = *head, *dp = NULL;

	if (*head == NULL)
		return (1);
	if ((*head)->next == NULL)
		return (1);
	while (1)
	{
		f = f->next->next;
		if (!f)
		{
			dp = s->next;
			break;
		}
		if (!f->next)
		{
			dp = s->next->next;
			break;
		}
		s = s->next;
	}
	reverse_listint(&dp);
	while (t && dp)
	{
		if (t->n == dp->n)
		{
			dp = dp->next;
			t = t->next;
		}
		else
		{
			return (0);
		}
	}
	if (!dp)
		return (1);
	return (0);
}

