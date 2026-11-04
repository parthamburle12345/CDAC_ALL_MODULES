"""
Title: NBA Player Biographical & Birthday Paradox Analysis 
Description: A modular Python exercise script for loading, sanitizing, and analyzing 
             NBA player birth dates to explore shared birthdays and player lookups.

"""

# Step 0: Import necessary libraries
# TODO: Import pandas, datetime, and any required modules
import pandas as pd


def phase_1_discovery_and_sanitization():
    """
    [Phase 1] Data Discovery, Column Standardization & Sanitization (5 Marks)
    - Goal: Load the NBA player CSV file.
    - Standardize column names (remove whitespace, lowercase, snake_case).
    - Sanitize 'Birth Date' into standard datetime format.
    """
    print("\n[PHASE 1] Discovery & Data Sanitization (5 Marks)")
    print("-" * 65)
    # TODO: Load CSV file using pandas (handling potential quote formatting)
    df = pd.read_csv("player_data.csv")

    # TODO: Standardize column headers (e.g., "Birth Date" -> "birth_date")
    df.columns = (df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace(r"[^\w_]", "", regex=True))  #u can avoid regex

    # Clean player name
    df["player_clean"] = df["player"].astype(str).str.rstrip("*").str.strip()

    # TODO: Parse 'birth_date' column into datetime objects using pd.to_datetime()
    df["birth_date"] = pd.to_datetime(df["birth_date"], format="%B %d %Y", errors="coerce")

    # TODO: Inspect dataset shape and check for missing birth dates
    print(f"Dataset shape: {df.shape}")
    print(f"Missing birth dates: {df['birth_date'].isna().sum()}")

    return df


def phase_2_birthday_paradox_analysis(df):
    """
    [Phase 2] Birthday Paradox & Distribution Analysis (10 Marks)
    - Goal: Analyze the distribution of birth dates across months and days.
    - Calculate and demonstrate the probability of shared birthdays (Birthday Paradox) 
      within subsets of NBA players.
    """
    print("\n[PHASE 2] Birthday Paradox & Date Distribution (10 Marks)")
    print("-" * 65)
    # TODO: Extract month and day components from 'birth_date'
    valid_df = df.dropna(subset=["birth_date"]).copy()
    valid_df["month"] = valid_df["birth_date"].dt.month
    valid_df["day"] = valid_df["birth_date"].dt.day
    valid_df["bday_md"] = valid_df["birth_date"].dt.strftime("%m-%d")

    # TODO: Count frequency of birthdays per calendar day
    bday_counts = valid_df["bday_md"].value_counts()
    print("Frequency of birthdays per calendar day (Top 5):")
    print(bday_counts.head())

    # TODO: Identify dates shared by multiple NBA players in the dataset
    shared_dates = bday_counts[bday_counts > 1]
    print(f"Total dates shared by multiple players: {len(shared_dates)}")

    return valid_df


def phase_3_player_lookup_system(df, player_name):
    """
    [Phase 3] Player Detail Retrieval (10 Marks)
    - Goal: Search for a specific player by name (case-insensitive or partial match).
    - Retrieve their biographical details (Position, College, Birth Date).
    """
    print(f"\n[PHASE 3] Player Lookup: Searching for '{player_name}' (10 Marks)")
    print("-" * 65)
    # TODO: Filter dataframe for the specified player name
    match = df[df["player_clean"].str.contains(player_name, case=False, na=False)]

    # TODO: Extract and return player details (Position, Ht, Wt, Colleges, Birth Date)
    if not match.empty:
        details = match.iloc[0]
        print(f"Player: {details['player']}")
        print(f"Position: {details.get('pos')}")
        print(f"Height: {details.get('ht')}")
        print(f"Weight: {details.get('wt')}")
        print(f"Colleges: {details.get('colleges')}")
        print(f"Birth Date: {details['birth_date']}")
        return details
    else:
        print("Player not found.")
        return None


def phase_4_shared_birthday_cohort(df, player_name):
    """
    [Phase 4] Shared Birthday Peer Finder (10 Marks)
    - Goal: Identify the target player's exact birth date.
    - List all other NBA players who share the exact same date of birth.
    """
    print(f"\n[PHASE 4] Shared Birthday Cohort for '{player_name}' (10 Marks)")
    print("-" * 65)
    # TODO: Retrieve the birth date of the target player from Phase 3
    player = phase_3_player_lookup_system(df, player_name)
    if player is not None and pd.notna(player["birth_date"]):
        target_date = player["birth_date"]

        # TODO: Query the dataset for all other players born on that exact month and day (or year)
        cohort = df[
            (df["birth_date"].dt.month == target_date.month)
            & (df["birth_date"].dt.day == target_date.day)
            & (df["player_clean"] != player["player_clean"])
        ]

        # TODO: Output the list of peer players sharing the birthday
        print(f"\nPlayers sharing birthday ({target_date.strftime('%B %d')}):")
        print(cohort[["player", "birth_date", "pos"]].to_string(index=False))
        return cohort
    return None


def phase_5_evaluation_and_summary(df):
    """
    [Phase 5] Evaluation & Reporting (5 Marks)
    - Goal: Summarize statistical findings on player longevity, birth months, 
      and birthday coincidences.
    """
    print("\n[PHASE 5] Evaluation & Summary Reporting (5 Marks)")
    print("-" * 65)
    # TODO: Print final summary statistics regarding dataset coverage and duplicate birthdays
    valid_bdate = df["birth_date"].dropna()
    print(f"Total players: {len(df)}")
    print(f"Total valid birth dates: {len(valid_bdate)}")

    bday_counts = valid_bdate.dt.strftime("%m-%d").value_counts()
    print(f"Unique birthdays: {len(bday_counts)}")
    print(f"Duplicate birthdays count: {(bday_counts > 1).sum()}")


# ==========================================
# THE FACADE FUNCTION (Orchestrator)
# ==========================================

def run_analytics_lifecycle():
    """
    Facade function coordinating the NBA analytics and birthday lookup workflow.
    """
    print("=" * 65)
    print("STARTING NBA BIRTHDAY & BIOGRAPHICAL LIFECYCLE (Out of 40 Marks)")
    print("=" * 65)
    
    # Target player to test lookup and shared birthdays
    target_player = "Kareem Abdul-Jabbar"
    
    # Executing phases chronologically
    df = phase_1_discovery_and_sanitization()
    df_analyzed = phase_2_birthday_paradox_analysis(df)
    phase_3_player_lookup_system(df, target_player)
    phase_4_shared_birthday_cohort(df, target_player)
    phase_5_evaluation_and_summary(df)


# ==========================================
# MAIN GUARD
# ==========================================
if __name__ == "__main__":
    run_analytics_lifecycle()
