# AUTH

POST   -> /auth/signup                     (Create account + auto create organization + default workspace)
POST   -> /auth/login                      (Login user)
POST   -> /auth/logout                     (Logout user)
GET    -> /auth/me                         (Get current authenticated user)
POST   -> /auth/refresh                    (Refresh access token)

---

# ORGANIZATION

GET    -> /organization                    (Get current organization)
PATCH  -> /organization                    (Update organization)

---

# WORKSPACES

POST   -> /workspaces                      (Create workspace)
GET    -> /workspaces                      (Get all user workspaces)
GET    -> /workspaces/:workspaceId         (Get workspace details)
PATCH  -> /workspaces/:workspaceId         (Update workspace)
DELETE -> /workspaces/:workspaceId         (Delete workspace)

---

# WORKSPACE MEMBERS

GET    -> /workspaces/:workspaceId/members                         (Get workspace members)
PATCH  -> /workspaces/:workspaceId/members/:memberId/role          (Update member role)
DELETE -> /workspaces/:workspaceId/members/:memberId               (Remove member)

---

# TEAMS

POST   -> /workspaces/:workspaceId/teams                          (Create team)
GET    -> /workspaces/:workspaceId/teams                          (Get workspace teams)
GET    -> /teams/:teamId                                          (Get team details)
PATCH  -> /teams/:teamId                                          (Update team)
DELETE -> /teams/:teamId                                          (Delete team)

POST   -> /teams/:teamId/members                                  (Add member to team)
GET    -> /teams/:teamId/members                                  (Get team members)
DELETE -> /teams/:teamId/members/:memberId                        (Remove team member)

---

# INVITATIONS

POST   -> /workspaces/:workspaceId/invitations                    (Invite user to workspace)
GET    -> /workspaces/:workspaceId/invitations                    (Get workspace invitations)

POST   -> /invitations/:token/accept                              (Accept invitation)
POST   -> /invitations/:token/reject                              (Reject invitation)

DELETE -> /invitations/:invitationId                              (Cancel invitation)

---

# ROLES

POST   -> /workspaces/:workspaceId/roles                          (Create role)
GET    -> /workspaces/:workspaceId/roles                          (Get workspace roles)
GET    -> /roles/:roleId                                          (Get role details)
PATCH  -> /roles/:roleId                                          (Update role)
DELETE -> /roles/:roleId                                          (Delete role)

---

# PERMISSIONS

GET    -> /permissions                                            (Get all permissions)

POST   -> /roles/:roleId/permissions                              (Assign permissions to role)
GET    -> /roles/:roleId/permissions                              (Get role permissions)

DELETE -> /roles/:roleId/permissions/:permissionKey               (Remove permission from role)