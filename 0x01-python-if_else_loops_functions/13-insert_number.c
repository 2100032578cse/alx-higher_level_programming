#include "lists.h"
/**
 * insert_node - insert node ant n
 * @head: the headnode
 * @number: number on which to insert
 * Return: the head
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *h = *head, *temp;

	temp = malloc(sizeof(listint_t));
	if (temp == NULL)
	{
		return (NULL);
	}
	temp->n = number;

	if (h == NULL || h->n >= number)
	{
		temp->next = h;
		*head = temp;
		return (temp);
	}
	while (h->next->n < number && h && h->next)
	{
		h = h->next;
	}
	temp->next = h->next;
	h->next = temp;
	return (temp);
}
