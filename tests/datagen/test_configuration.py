"""
Unit tests for Column and Entity schema validation classes.

These tests verify:
- Column initialization rules
- Numeric range constraints
- Duplicate column handling in Entity
- Row-level validation logic
"""

import pytest
from datagen.configuration import Column, Entity

@pytest.fixture
def person_entity():
    return Entity(
        name="Person",
        columns=[
            Column(name="id", dtype=int, nullable=False),
            Column(name="age", dtype=int, value_range=(0, 120)),
        ],
    )

def test_column_numeric_pass():
    age_col = Column(name="age", dtype=int, value_range=(0, 120), nullable=False)

    assert age_col.validate(25) is True
    assert age_col.validate(-5) is False
    assert age_col.validate(130) is False

def test_column_non_numeric_value_range_fails():
    with pytest.raises(ValueError, match="value_range can only be used with numeric types"):
        Column(name="name", dtype=str, value_range=(0, 100))
        
def test_column_value_range_min_greater_than_max_fails():
    with pytest.raises(ValueError, match="min cannot be greater than max"):
        Column(name="score", dtype=int, value_range=(100, 0))
        
def test_entity_creation_with_unique_columns():
    cols = [
        Column(name="id", dtype=int, nullable=False),
        Column(name="name", dtype=str),
    ]

    entity = Entity(name="Person", columns=cols)

    assert entity.get_column("id") is cols[0]
    assert entity.get_column("name") is cols[1]


def test_entity_duplicate_columns_on_init_fails():
    cols = [
        Column(name="id", dtype=int),
        Column(name="id", dtype=str),
    ]

    with pytest.raises(ValueError, match="Duplicate column names"):
        Entity(name="Person", columns=cols)


def test_entity_add_column_duplicate_name_fails(person_entity):
    with pytest.raises(ValueError, match="already exists"):
        person_entity.add_column(Column(name="id", dtype=str))


def test_entity_get_column_returns_none_when_missing(person_entity):
    assert person_entity.get_column("unknown") is None


def test_entity_validate_row_passes(person_entity):
    row = {"id": 1, "age": 35}

    assert person_entity.validate_row(row) is True


def test_entity_validate_row_fails_when_required_column_missing(person_entity):
    row = {"age": 30}

    assert person_entity.validate_row(row) is False


def test_entity_validate_row_fails_when_value_invalid_range(person_entity):
    row = {"id": 1, "age": 200}

    assert person_entity.validate_row(row) is False


def test_entity_validate_row_fails_when_type_invalid(person_entity):
    row = {"id": 1, "age": "Smith"}

    assert person_entity.validate_row(row) is False