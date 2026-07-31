from .BaseDataModel import BaseDataModel
from .enums.DataBaseEnum import DataBaseEnum
from .schemes_db import Project

class ProjectModel(BaseDataModel):
    def __init__(self, db_client: object):
        super().__init__(db_client=db_client)
        self.collection = DataBaseEnum.COLLECTION_PROJECT_NAME.value
        self.collection = db_client[self.collection]
    @classmethod
    async def create_instance(cls, db_client: object):
        instance = cls(db_client=db_client)
        await instance.init_collection()
        return instance

    async def init_collection(self):
        all_collections= await self.db_client.list_collection_names()
        if DataBaseEnum.COLLECTION_PROJECT_NAME.value not in all_collections:
            self.collection =self.db_client[DataBaseEnum.COLLECTION_PROJECT_NAME.value]
            indexes = Project.get_project_indexes()
            for index in indexes:
                await self.collection.create_index(
                    index['key'],
                    name=index['name'], 
                    unique=index['unique']
                    )



    async def create_project(self, project: Project):
        result = await self.collection.insert_one(project.dict(by_alias=True,exclude_unset=True))
        project.id = result.inserted_id
        return project
    async def get_or_create_project(self, project_id: str):
        project_data = await self.collection.find_one({"project_id": project_id})
        if project_data is None:
            new_project = Project(project_id=project_id)
            project=await self.create_project(project=new_project)
            return project
        return Project(**project_data)
    async def get_all_projects(self, page: int, page_size: int):
        total_documents = await self.collection.count_documents({})
        total_pages = total_documents// page_size
        if total_documents % page_size > 0:
            total_pages += 1
        projects_cursor = self.collection.find().skip((page - 1) * page_size).limit(page_size)
        projects = []
        async for project_data in projects_cursor:
            projects.append(Project(**project_data))
        return projects,total_pages
        