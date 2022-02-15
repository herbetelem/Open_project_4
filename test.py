 # def generate_round(self):
    #     self.sort_by_rank()
    #     index_match = 0
    #     for player in self.players:
    #         i = 0
    #         while not player.choosed and i < len(self.players):
    #             if player.id != self.players[i].id and \
    #                     self.players[i] not in player.matched and \
    #                     player.pool != self.players[i].pool and \
    #                     not self.players[i].choosed:
    #                 player.choosed = True
    #                 self.players[i].choosed = True
    #                 self.match[index_match][0] = player
    #                 self.match[index_match][1] = self.players[i]
    #                 index_match += 1
    #             i += 1
    #         i = 0
    #         while not player.choosed and i < len(self.players):
    #             if player.id != self.players[i].id:
    #                 if self.players[i] not in player.matched:
    #                     if not self.players[i].choosed:
    #                         player.choosed = True
    #                         self.players[i].choosed = True
    #                         self.match[index_match][0] = player
    #                         self.match[index_match][1] = self.players[i]
    #                         index_match += 1
    #             i += 1
    #     for player in self.players:
    #         if not player.choosed:
    #             print("toto")
