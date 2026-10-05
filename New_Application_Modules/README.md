# 🌟 New Application Modules (Update v2.1)

This directory isolates and documents the **4 brand new application modules** introduced in this update, introduced in the latest ClashBot-Pro v2.1 update.

---

## 📑 Module Index
1. [`equipment_upgrade.py`](#1-equipment_upgradepy-hero-equipment-automation) - Blacksmith Hero Equipment auto-upgrader
2. [`rush_bh.py`](#2-rush_bhpy-builder-hall-rush-engine) - Builder Hall progression & B.O.B unlocker
3. [`startup_checks.py`](#3-startup_checkspy-special-event--dialogue-resolver) - Pre-home village modals, WWE chests & card handler
4. [`ranked_unlock.py`](#4-ranked_unlockpy-ranked-battle-unlock-sequence) - Automated Ranked Battles macro unlocker

---

## 1. `equipment_upgrade.py`: Hero Equipment Automation

### Purpose
Automates navigation into the Blacksmith structure, inspects all unlocked Hero equipment, evaluates Common vs. Epic gear, and executes upgrades using Shiny Ore, Glowy Ore, and Starry Ore.

### Supported Heroes
1. **Barbarian King**
2. **Archer Queen**
3. **Minion Prince** *(Supercell's newest hero)*
4. **Grand Warden**
5. **Royal Champion**

### Key Constants & Regions
```python
# Daily check interval
EQUIP_CHECK_INTERVAL_SECONDS = 86400

# Hero tab touch coordinates (6 tabs)
EQUIP_HERO_TAB_POINTS = [
    (163, 491), (207, 490), (256, 490),
    (304, 490), (349, 492), (396, 492)
]

# Coordinate bounding boxes for equipment categories
EQUIP_COMMON_REGION = (114, 527, 333, 748)
EQUIP_EPIC_REGION = (333, 528, 558, 749)
EQUIP_CURRENTLY_EQUIPPED_REGION = (136, 339, 1461, 444)
EQUIP_CLOSE_BLACKSMITH_POINT = (1530, 97)
EQUIP_BADGE_TAP_OFFSET = (-15, 15)

# Multi-scale OpenCV matching configuration
EQUIP_UPGRADE_MATCH_THRESHOLD = 0.7
EQUIP_UPGRADE_MATCH_SCALES = [0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0, 1.05, 1.1, 1.15, 1.2]
```

### Public API Functions
- `run(adb, vision, cfg, pause_if_needed=None, profile_name=None)`: Main entry point for the equipment upgrade loop.
- `run_hero_priority(adb, vision, hero_settings, pause_if_needed=None)`: Iterates through heroes by user priority.
- `run_currently_equipped(adb, vision, pause_if_needed=None)`: Upgrades gear currently equipped in battle slots.
- `should_run_equipment_check(profile_name=None)`: Throttles checks to once every 24 hours.

---

## 2. `rush_bh.py`: Builder Hall Rush Engine

### Purpose
Implements a fast-track Builder Base progression strategy specifically tuned to meet the prerequisites for unlocking the **6th Builder (B.O.B)** with minimal waste.

### Priority Ladders
```python
BUILDER_HALL_KEY = 'bb_upgrade_builder_hall'

# Storage & Laboratory upgrades required before BH bump
MAIN_LADDER = [
    'bb_upgrade_gold_storage',
    'bb_upgrade_elixir_storage',
    'bb_upgrade_star_laboratory'
]

# Troops focused for level 18 requirement
RESEARCH_CHAIN = [
    'bb_research_baby_dragon',
    'bb_research_sneaky_archer',
    'bb_research_raged_barbarian'
]

# Hero priority (Level 45 combined requirement)
HERO_PRIORITY = ['battlecopter', 'battlemachine']
TROOP_PRIORITY = ['Baby Dragon', 'Archer', 'Barbarian']

# Secondary defensive structures
LOW_PRIORITY = [
    'bb_upgrade_battle_machine',
    'bb_upgrade_battle_copter',
    'bb_upgrade_multi_mortar'
]
BACKUP = ['bb_upgrade_clock_tower', 'bb_upgrade_gem_mine']
LAST_RESORT_GROUPS = ['__GROUP:Buildings__', '__GROUP:Defences__']
```

---

## 3. `startup_checks.py`: Special Event & Dialogue Resolver

### Purpose
Runs immediately after client launch and before the standard Home Village loop. It dismisses promotional cards, collects WWE event chests, accepts return bonuses, and settles desyncs.

### Public API Functions
- `run_pre_home_village_checks(vision, settle_frame=None, maintenance_wait_seconds=0)`: Pre-flight screen scanner.
- `resolve_open_card_or_chest(vision, tap_fn, save_screenshot_fn, screen=None, timeout=0.0, poll_interval=0.5)`: Identifies mystery chests/cards, taps to reveal rewards, and dismisses the modal.
- `resolve_card_continue(vision, tap_fn, timeout=10.0, poll_interval=0.3)`: Locates and taps the green `townhall_continue.png` button.
- `settle_until_home(vision, timeout_seconds=60, extend_seconds=30, maintenance_wait_seconds=0, stop_on=None, pause_fn=None)`: Monitors frame changes until the Home Village coordinate canvas is settled.
- `_handle_return_bonus(vision, settle_frame=None)`: Automates welcome-back loot claims.

---

## 4. `ranked_unlock.py`: Ranked Battle Unlock Sequence

### Purpose
Executes the dialogue taps and menu interactions needed to initialize and unlock the Ranked Battles feature on fresh accounts.

### Macro Sequence
- `run_ranked_unlock_script()`: Coordinates tap steps through `_RANKED_UNLOCK_STEPS` with calibrated micro-delays:
  ```python
  _RANKED_UNLOCK_STEPS = [
      (1713, 'tap', 524, 538),
      (1543, 'tap', 524, 538),
      (1903, 'tap', 579, 521),
      (2034, 'tap', 872, 692),
      (1200, 'tap', 720, 480)
  ]
  ```

---

## 🔗 Integration

These modules reside alongside the existing 76 modules in `releases\v2.1-update\Source\`. They are loaded dynamically by `ui\bot_worker.py` and invoked based on user configuration in `profiles/config.json`.
