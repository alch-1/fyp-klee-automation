#include <stdio.h>
#include <string.h>
struct game
{
  char game_name[50];
  int number_of_players;
};  // Note the semicolon

int main()
{
  struct game g;

  strcpy(g.game_name, "Cricket");
  g.number_of_players = 11;

  printf("Name of game: %s\n", g.game_name);
  printf("Number of players: %d\n", g.number_of_players);

  return 0;
}
