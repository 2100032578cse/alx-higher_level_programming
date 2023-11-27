#include "lists.h"
/**
 * check_cycle - checks loops
 * @list: list given
 * Return: 1 or 0
*/
int check_cycle(listint_t *list)
{
	listint_t *f, *s;

	if (list == NULL)
		return (0);
	if (list->next == NULL)
		return (0);
	s = list->next;
	f = list->next->next;
	while (s && f && f->next)
	{
		if (s == f)
		{
			return (1);
		}
		s = s->next;
		f = f->next->next;
	}
	return (0);
}
