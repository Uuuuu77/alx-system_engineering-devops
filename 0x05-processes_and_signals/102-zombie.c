#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

/**
 * infinite_while - Entry point-> Its a infinite sleep.
 * Return: 0 (Success)
*/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Entry point-> It creates 5 zombie processes.
 * Return: 0 (Success), 1 (Fail)
*/
int main(void)
{
	int x;
	pid_t child_pid;

	for (x = 0; x < 5; x++)
	{
		child_pid = fork();
		if (child_pid == 0)
		{
			/*printf("Zombie process created, PID: %d\n", child_pid);*/
			exit(0);
		}
		else if (child_pid > 0)
		{
			printf("Zombie process created, PID: %d\n", child_pid);
		}
		else
		{
			perror("fork");
			exit(1);
		}
	}
	infinite_while();

	return (0);
}
