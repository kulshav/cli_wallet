import pytest

from storage.core import StorageManager


@pytest.fixture
def storage_instance():
    storage_instance = StorageManager()

    yield storage_instance


@pytest.fixture
def restart_storage(storage_instance):
    storage_instance._drop_storage()
    storage_instance._create_storage()

