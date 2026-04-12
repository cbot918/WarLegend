
table user
    - id: integer (primary key)
    - username: string
    - password: string
    - email: string
    - created_at: timestamp
    - updated_at: timestamp

table character
    - id: integer (primary key)
    - name: string
    - health: integer
    - job_level: integer
    - combat_score: integer
    - command_score: float
    - job_class: integer
    - user_id: integer (foreign key referencing user.id)
    - created_at: timestamp
    - updated_at: timestamp

table legion
    - id: integer (primary key)
    - character_id: integer (foreign key referencing character.id)
    - battle_score: integer
    - legion_count: integer

table job_class