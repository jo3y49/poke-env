import asyncio

from poke_env.player import RandomPlayer, Player
from poke_env import PlayerConfiguration, ShowdownServerConfiguration
from poke_env.player.battle_order import (
    BattleOrder,
    DefaultBattleOrder,
    DoubleBattleOrder,
)

class MetroPlayer(Player):
    def choose_move(self, battle) -> DoubleBattleOrder:
        return self.choose_random_doubles_move(battle)

async def main():
    team_1="""
Sableye @ Sablenite  
Ability: Dauntless Shield  
Tera Type: Dark  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD  
Relaxed Nature  
IVs: 0 Spe  
- Metronome  

Ting-Lu @ Weakness Policy  
Ability: Defiant  
Tera Type: Ghost  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD / 252 Spe  
Brave Nature  
- Metronome  
"""
    team_2 = """
Heracross-Mega @ Choice Band  
Ability: Defiant  
Tera Type: Bug  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD / 252 Spe  
Adamant Nature  
- Metronome 

Heracross-Mega @ Choice Band  
Ability: Defiant  
Tera Type: Bug  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD / 252 Spe  
Adamant Nature  
- Metronome   
"""
    team_3 = """
Venusaur-Mega @ Weakness Policy  
Ability: Beads of Ruin  
Tera Type: Grass  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD  
Relaxed Nature  
IVs: 0 Spe  
- Metronome  

Gengar-Mega @ Choice Specs  
Ability: Hadron Engine  
Tera Type: Ghost  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD / 252 Spe  
Mild Nature  
- Metronome  
"""
    team_4 = """
Ting-Lu @ Weakness Policy  
Ability: Sword of Ruin  
Tera Type: Ghost  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD  
Brave Nature  
IVs: 0 Spe  
- Metronome  

Ting-Lu @ Weakness Policy  
Ability: Defiant  
Tera Type: Ghost  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD / 252 Spe  
Brave Nature  
- Metronome 
"""
    team_5 = """
Ting-Lu @ Weakness Policy  
Ability: Sword of Ruin  
Tera Type: Ghost  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD  
Brave Nature  
IVs: 0 Spe  
- Metronome  

Ting-Lu @ Weakness Policy  
Ability: Defiant  
Tera Type: Ghost  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD / 252 Spe  
Brave Nature  
- Metronome 
"""
    team_6 = """
Pikachu-Starter @ Light Ball  
Ability: Imposter  
Tera Type: Ghost  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD / 252 Spe  
Naive Nature  
- Metronome  

Pikachu-Starter @ Light Ball  
Ability: Imposter  
Tera Type: Ghost  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD / 252 Spe  
Naive Nature  
- Metronome 
"""
    team_7 = """
Blissey @ Leppa Berry  
Ability: Imposter  
Tera Type: Ghost  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD / 252 Spe  
Sassy Nature  
- Metronome  

Blissey @ Leppa Berry  
Ability: Imposter  
Tera Type: Ghost  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD  
Sassy Nature  
IVs: 0 Spe  
- Metronome  
"""
    team_8 = """
Xurkitree @ Choice Specs  
Ability: Hadron Engine  
Tera Type: Ghost  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD / 252 Spe  
Rash Nature  
- Metronome  

Venusaur-Mega @ Weakness Policy  
Ability: Beads of Ruin  
Tera Type: Grass  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD  
Relaxed Nature  
IVs: 0 Spe  
- Metronome  
"""
    team_9 = """
Ting-Lu @ Mirror Herb  
Ability: Defiant  
Tera Type: Ghost  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD / 252 Spe  
Adamant Nature  
- Metronome  

Sableye @ Sablenite  
Ability: Intimidate  
Tera Type: Dark  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD  
Relaxed Nature  
IVs: 0 Spe  
- Metronome  
"""

    bug_config = PlayerConfiguration("powerbugs", "metrobug")
    my_player_config = PlayerConfiguration("Jo3y49", "@%Wg!(Z0!)Wa")
    
    player1 = MetroPlayer(
        battle_format="gen9metronomebattle",
        team = team_7,
        start_timer_on_battle_start=True,
        player_configuration=bug_config,
        server_configuration=ShowdownServerConfiguration,
        max_concurrent_battles=50,
    )
    player2 = MetroPlayer(
        battle_format="gen9metronomebattle",
        team = team_9,
        start_timer_on_battle_start=True,
    )

    battles = 10
    

    await player1.ladder(battles)

    print("Player 1 won", player1.n_won_battles, "/", battles ,"battles")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())