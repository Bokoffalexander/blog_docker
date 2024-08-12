import pytest
import logging

logger = logging.getLogger(__name__)


@pytest.mark.django_db
def test_create_blog(api_client) -> None:
    """
    Test the create a new post API
    :param api_client:
    :return: None
    """
    payload = {
        "title": "My Clothes",
        "content": "My clothes are in the washing machine",
        "is_published": "true"
    }

    # Create a new post
    response_create = api_client.post("/api/v1/bloglist/", data=payload, format="json")
    task_id = response_create.data["post"]["id"]
    logger.info(f"Created a new post with id: {post_id}")
    logger.info(f"Response: {response_create.data}")
    assert response_create.status_code == 201
    assert response_create.data["post"]["title"] == payload["title"]

    # Read all posts
    response_read = api_client.get(f"/api/v1/bloglist/", format="json")
    logger.info(f"Response: {response_read.data}")
    assert response_read.status_code == 200
    assert response_read.data["post"]["title"] == payload["title"]


@pytest.mark.django_db
def test_patch_blog(api_client) -> None:
    """
    Test the update the post API
    :param api_client:
    :return: None
    """
    payload = {
        "title": "Trim the Lawn",
        "content": "Trim the lawn with the lawnmower",
        "is_published": "true"
    }

    # Create a new post
    response_create = api_client.post("/api/v1/bloglist/", data=payload, format="json")
    blog_id = response_create.data["post"]["id"]
    logger.info(f"Created a mew post with id: {blog_id}")
    logger.info(f"Response: {response_create.data}")
    assert response_create.status_code == 201
    assert response_create.data["post"]["title"] == payload["title"]

    # Update the post
    payload["title"] = "Cut the grass"
    response_update = api_client.patch(
        f"/api/v1/bloglist/{blog_id}", data=payload, format="json"
    )
    logger.info(f"Updated blog with id: {blog_id}")
    logger.info(f"Response: {response_update.data}")
    assert response_update.status_code == 200
    assert response_update.data["post"]["title"] == payload["title"]

    # This blog doesn't exist
    response_update = api_client.patch(
        f"/api/v1/bloglist/{task_id + '1'}", data=payload, format="json"
    )
    logger.info(f"Updated blog with id: {blog_id + '1'}")
    logger.info(f"Response: {response_update.data}")
    assert response_update.status_code == 404


@pytest.mark.django_db
def test_delete_task(api_client) -> None:
    """
    Test the delete task API
    :param api_client:
    :return: None
    """
    payload = {
        "title": "Cook healthy food",
        "content": "Cook healthy food for the family with high protein and low fat",
    }

    # Create a task
    response_create = api_client.post("/api/tasks/", data=payload, format="json")
    task_id = response_create.data["task"]["id"]
    logger.info(f"Created task with id: {task_id}")
    logger.info(f"Response: {response_create.data}")
    assert response_create.status_code == 201
    assert response_create.data["task"]["title"] == payload["title"]

    # Delete the task
    response_delete = api_client.delete(f"/api/tasks/{task_id}", format="json")
    assert response_delete.status_code == 204

    # Read the task
    response_read = api_client.get(f"/api/tasks/{task_id}", format="json")
    assert response_read.status_code == 404

    # Task doesn't exist
    response_delete = api_client.delete(f"/api/tasks/{task_id + '1'}", format="json")
    assert response_delete.status_code == 404