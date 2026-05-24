from enum import Enum
class ProjectStatus(str,Enum):
    CREATED="CREATED"
    PLANNING="PLANNING"
    IN_PROGRESS="IN_PROGRESS"
    COMPLETED="COMPLETED"
    