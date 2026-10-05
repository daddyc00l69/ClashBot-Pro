# Source Recovery & Reverse-Engineering Audit Report: ClashBot-Pro (New Update)

## 1. Executive Statement of Recovery

This report documents the decompilation, carving, asset extraction, and source recovery process conducted on the updated **ClashBot-Pro** binary (`ClashBot-Pro Application Engine`, 97,794,560 bytes).

In accordance with strict reverse-engineering principles:
- **Zero modification to binaries:** Both the original binary and `ClashBot-Pro Application Engine` remain strictly untouched with original byte size and SHA-256 hashes preserved.
- **Byte-accurate carving:** All 80 application modules were carved from Nuitka constants blob #3 in `gui.dll` (at offset `0x04C13F50`, size 14,910,416 bytes) with exact `PY015394` PyArmor container payloads.
- **100% Syntax & Import Validation:** All 80 Python source modules in `Recovered_Source_New_Update\Source\` pass `python -m py_compile` with 0 errors and load cleanly under CPython 3.10 with `pyarmor_runtime_015394`.

---

## 2. Comparative Recovery Status Matrix

| Component / Subsystem | Previous Version | New Update Version | Delta / Changes |
|---|---|---|---|
| **Outer Binary (`ClashBot-Pro Application Engine`)** | 97,402,368 bytes | **97,794,560 bytes** | +392,192 bytes (+383 KB) |
| **Outer Binary SHA-256** | `6886e8ea3f3f...` | `37189aa94101e4ee99c727181c0c0576390a78fc7bb35cbb2c73eb26ae4624b4` | Updated payload |
| **Carved Payload Size (Uncompressed)**| 314.43 MB (1,202 files)| **314.86 MB (1,237 files)** | **+35 files** (+440 KB) |
| **Core Native DLL (`gui.dll`)** | 94,558,208 bytes | **94,692,864 bytes** | +134,656 bytes (+131.5 KB) |
| **Nuitka Constants Resource (ID 3)** | 14,788,499 bytes | **14,910,416 bytes** | +121,917 bytes |
| **Nuitka Blob Chunks** | 876 chunks | **880 chunks** | **+4 new module chunks** |
| **Application Modules (PyArmor)** | 76 modules | **80 modules** | **+4 new application modules** |
| **Visual OpenCV Templates** | 992 templates | **1,026 templates** | **+35 new templates** (-1 obsolete) |
| **Encrypted Coordinate Anchors** | 862 fixed points | **906 fixed points** | **+44 new fixed points** |
| **Encrypted Asset SHA-256** | `3b6c3443074d...` | `401ddd06db9b1600cdc3a2c6726816a650717675e5520ce4399f2629726a23a9` | Re-encrypted with updated anchors |
| **Localization Files** | 11 languages | **11 languages** | Preserved (ar, de, en, es, fr, hi, id, pt-br, ru, tl, tr) |
| **PyArmor Runtime ID** | `015394` | `015394` | Fully compatible |
| **Clean Syntax Validation** | 100% (77/77 files) | **100% (80/80 files)** | **0 syntax errors** |

---

## 3. Detailed Audit of New Application Modules

The new update introduces **4 brand new application modules**:

### 3.1 `equipment_upgrade.py` (Blacksmith Hero Equipment Automation)
- **Role:** Automates Hero Equipment upgrading inside the Blacksmith interface.
- **Hero Order Supported:**
  1. Barbarian King
  2. Archer Queen
  3. Minion Prince *(Supercell's newest hero)*
  4. Grand Warden
  5. Royal Champion
- **Key Parameters & Constants:**
  - `EQUIP_HERO_TAB_POINTS`: 6 hero tabs at screen coordinates `[(163, 491), (207, 490), (256, 490), (304, 490), (349, 492), (396, 492)]`.
  - `EQUIP_COMMON_REGION`: Bounding box `(114, 527, 333, 748)` for common equipment scanning.
  - `EQUIP_EPIC_REGION`: Bounding box `(333, 528, 558, 749)` for epic equipment scanning.
  - `EQUIP_CURRENTLY_EQUIPPED_REGION`: Bounding box `(136, 339, 1461, 444)`.
  - `EQUIP_CHECK_INTERVAL_SECONDS`: 86,400s (daily check cadence).
  - Multi-scale template matching scales: `[0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0, 1.05, 1.1, 1.15, 1.2]` with threshold `0.7`.
- **Public Functions:**
  - `run(adb, vision, cfg, pause_if_needed=None, profile_name=None)`
  - `run_hero_priority(adb, vision, hero_settings, pause_if_needed=None)`
  - `run_currently_equipped(adb, vision, pause_if_needed=None)`
  - `should_run_equipment_check(profile_name=None)`

### 3.2 `rush_bh.py` (Builder Hall Rush Automation)
- **Role:** Automated progression path for fast-tracking Builder Base levels to unlock the 6th builder (B.O.B).
- **Core Priority Ladders:**
  - `BUILDER_HALL_KEY`: `'bb_upgrade_builder_hall'`
  - `MAIN_LADDER`: `['bb_upgrade_gold_storage', 'bb_upgrade_elixir_storage', 'bb_upgrade_star_laboratory']`
  - `RESEARCH_CHAIN`: `['bb_research_baby_dragon', 'bb_research_sneaky_archer', 'bb_research_raged_barbarian']`
  - `HERO_PRIORITY`: `['battlecopter', 'battlemachine']`
  - `TROOP_PRIORITY`: `['Baby Dragon', 'Archer', 'Barbarian']`
  - `LOW_PRIORITY`: `['bb_upgrade_battle_machine', 'bb_upgrade_battle_copter', 'bb_upgrade_multi_mortar']`
  - `BACKUP`: `['bb_upgrade_clock_tower', 'bb_upgrade_gem_mine']`

### 3.3 `startup_checks.py` (Pre-Home Village & Special Event Handler)
- **Role:** Handles special reward modals, returning player bonuses, and seasonal events before the Home Village main loop engages.
- **Key Capabilities:**
  - `run_pre_home_village_checks(vision, settle_frame=None, maintenance_wait_seconds=0)`
  - `resolve_open_card_or_chest(...)`: Automatically detects and taps to open WWE event chests and seasonal mystery cards.
  - `resolve_card_continue(...)`: Taps through card continuation buttons.
  - `_handle_return_bonus(vision, settle_frame=None)`: Resolves welcome-back bonus dialogues.
  - `settle_until_home(...)`: Ensures the game camera has fully transitioned to the Home Village canvas.

### 3.4 `ranked_unlock.py` (Ranked Battle Macro Runner)
- **Role:** Automates the prerequisite dialogues and unlock sequence required to access Ranked Battles.
- **Public Functions:**
  - `run_ranked_unlock_script()`
  - Sequence steps defined in `_RANKED_UNLOCK_STEPS`.

---

## 4. New OpenCV Templates Inventory (35 Total)

The update introduces 35 new graphic recognition templates in `Recovered_Source_New_Update\Resources\templates\`:

1. **Equipment Upgrade Buttons:**
   - `eq_upgrade_button.png`
   - `eq_confirm_button.png`
2. **Capital Raid Spell Icons:**
   - `capitalraid\raid_graveyard.png`
   - `capitalraid\raid_heal.png`
   - `capitalraid\raid_jump.png`
   - `capitalraid\raid_rage.png`
3. **Capital Raid Digits (0 through 9):**
   - `digits\raid\0.png` through `digits\raid\9.png`
4. **Seasonal & Event Troops:**
   - `tabs\event_barcher.png`
   - `tabs\event_giantskeleton.png`
   - `tabs\event_hogwizard.png`
   - `tabs\event_pumpkinbarbarian.png`
   - `tabs\event_royalghost.png`
   - `tabs\event_skeletonbarrel.png`
   - `tabs\event_totemthrower.png`
   - `tabs\event_witchgolem.png`
5. **Builder Base & Upgrades:**
   - `upgrades-research\bb_upgrade_builder_hall.png`
   - `upgrades-research\bb_upgrade_clock_tower.png`
   - `upgrades-research\home_research_angry_spell.png`
   - `upgrades-research\home_research_ruin_witch.png`
   - `upgrades-research\ui\upgrade_weapon.png`
6. **Clan War Leagues (CWL) & Social:**
   - `war\start_cwl.png`
   - `war\cwl_warinfo.png`
   - `accept_join_request.png`
7. **Special Modals & Ranked:**
   - `wwe_chest.png`
   - `ranked_unlocked.png`
   - `townhall_continue.png`

---

## 5. Decrypted Coordinate Anchors (`fixed_points_source.py`)

Using the AES-256-GCM cipher suite and master key:
- Decrypted from: `Resources\assets\fixed_points_data.enc`
- Total constants: **906 coordinates and regions** (increased from 862)
- 44 new points cover:
  - Hero equipment modal boundaries
  - Blacksmith close button anchors `(1530, 97)`
  - CWL map navigation anchors
  - WWE chest click points
  - Ranked unlock progression taps

All 906 constants are exported cleanly as a standard Python module in:
`releases\v2.1-update\Source\fixed_points_source.py` with full `__all__` list.

---

## 6. Access & File Paths

The recovered new update source is organized under:

- **Source Tree:** [`releases/v2.1-update`](file:///c:/Users/aradh/Desktop/Auto%20Clash%20clone%20Vip/releases/v2.1-update)
- **New Application Modules:** [`releases/v2.1-update/New_Application_Modules`](file:///c:/Users/aradh/Desktop/Auto%20Clash%20clone%20Vip/releases/v2.1-update/New_Application_Modules)
- **Original Binary:** [`binaries/v2.1-update/ClashBot-Pro Application Engine`](file:///c:/Users/aradh/Desktop/Auto%20Clash%20clone%20Vip/binaries/v2.1-update/ClashBot-Pro Application Engine)

### Quickstart Execution
To run the updated bot from source:
1. Double-click [`run_v2_update.bat`](file:///c:/Users/aradh/Desktop/Auto%20Clash%20clone%20Vip/run_v2_update.bat) (or `run_bot.bat`) in the project root.
2. Or run:
   ```cmd
   cd releases\v2.1-update\Source
   python ..\Project\run.py
   ```
3. To run integrity tests:
   ```cmd
   cd releases\v2.1-update\Project
   python test_suite.py
   ```
