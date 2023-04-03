import asyncio
import numpy as np
from poke_env.player import RandomPlayer, Player
from poke_env import PlayerConfiguration, ShowdownServerConfiguration
    
class MaxDamagePlayer(Player):
    def choose_move(self, battle):
        if battle.available_moves:
            best_move = max(battle.available_moves, key=lambda move: move.base_power)
            return self.create_order(best_move)
        else:
            return self.choose_random_move(battle)
        
    def teampreview(self, battle):
        mon_performance = {}

        for i, mon in enumerate(battle.team.values()):
            mon_performance[i] = np.mean([
                teampreview_performance(mon, opp)
                for opp in battle.opponent_team.values()
            ])

        ordered_mons = sorted(mon_performance, key = lambda k: -mon_performance[k])

        return "/team " + ''.join([str(i + 1) for i in ordered_mons])
        
def teampreview_performance(mon_a, mon_b):
    a_on_b = b_on_a = -np.inf
    for type_ in mon_a.types:
        if type_:
            a_on_b = max(a_on_b, type_.damage_multiplier(*mon_b.types))
    for type_ in mon_b.types:
        if type_:
            b_on_a = max(b_on_a, type_.damage_multiplier(*mon_a.types))

    return a_on_b - b_on_a

# class SuperEffectivePlayer(Player):
#     def choose_move(self, battle):
#         if battle.available_moves:
        
            


async def main():
    team_1="""
Azumarill @ Choice Band  
Ability: Huge Power  
EVs: 252 HP / 252 Atk / 4 SpD  
Adamant Nature  
- Liquidation  
- Aqua Jet  
- Play Rough  
- Superpower  

Garchomp @ Rocky Helmet  
Ability: Rough Skin   
EVs: 252 Atk / 4 SpA / 252 Spe  
Naive Nature  
- Stealth Rock  
- Earthquake  
- Stone Edge  
- Draco Meteor  

Corviknight @ Leftovers  
Ability: Pressure   
EVs: 252 HP / 4 Atk / 252 Def  
Impish Nature  
- Brave Bird  
- U-turn  
- Roost  
- Defog  

Dragapult @ Choice Specs  
Ability: Infiltrator  
EVs: 252 SpA / 4 SpD / 252 Spe  
Modest Nature  
- Shadow Ball  
- Draco Meteor  
- Fire Blast  
- U-turn  

Dragonite @ Heavy-Duty Boots  
Ability: Multiscale  
EVs: 252 Atk / 4 SpD / 252 Spe  
Adamant Nature  
- Dragon Dance  
- Extreme Speed  
- Earthquake  
- Roost  

Hydreigon @ Choice Specs  
Ability: Levitate  
EVs: 252 SpA / 4 SpD / 252 Spe  
Timid Nature  
IVs: 0 Atk  
- Dark Pulse  
- Draco Meteor  
- Earth Power  
- Flash Cannon
"""
    team_2 ="""
Amoonguss @ Heavy-Duty Boots  
Ability: Regenerator   
EVs: 248 HP / 252 Def / 8 SpD  
Bold Nature  
IVs: 0 Atk  
- Spore  
- Giga Drain  
- Sludge Bomb  
- Foul Play  

Cinderace @ Heavy-Duty Boots  
Ability: Blaze  
EVs: 252 Atk / 4 SpD / 252 Spe  
Jolly Nature  
- Pyro Ball  
- U-turn  
- Sucker Punch  
- Court Change  

Hatterene (F) @ Leftovers  
Ability: Magic Bounce   
EVs: 252 HP / 4 Atk / 252 SpA  
Quiet Nature  
- Calm Mind  
- Draining Kiss  
- Psyshock  
- Nuzzle  

Dragapult @ Choice Specs  
Ability: Infiltrator  
EVs: 252 SpA / 4 SpD / 252 Spe  
Modest Nature  
IVs: 0 Atk  
- Shadow Ball  
- Draco Meteor  
- Fire Blast  
- Thunderbolt  

Volcarona @ Life Orb  
Ability: Flame Body  
EVs: 252 SpA / 4 SpD / 252 Spe  
Modest Nature  
IVs: 0 Atk  
- Quiver Dance  
- Fiery Dance  
- Bug Buzz  
- Psychic  

Toxapex @ Leftovers  
Ability: Regenerator   
EVs: 252 HP / 252 Def / 4 SpA  
Bold Nature  
IVs: 0 Atk  
- Toxic  
- Toxic Spikes  
- Surf  
- Haze    
"""
    my_player_config = PlayerConfiguration("Jo3y49", "@%Wg!(Z0!)Wa")
    bug_config = PlayerConfiguration("powerbugs", "metrobug")

    cole_username = "PieDotNet2"
    
    max_damage_player = MaxDamagePlayer(
        battle_format="gen9ou",
        team=team_1,
    )

    max_damage_player2 = RandomPlayer(
        battle_format="gen9ou",
        team=team_2,
    )

    await max_damage_player.battle_against(max_damage_player2, n_battles=100)

    print(
        "Player 1 won %d / 100 battles"
        % max_damage_player.n_won_battles
    )

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())