def create_graph(projects, dependencies):
   project_graph = {}
   for project in projects:
       project_graph[project] = []
   for pairs in dependencies:
       project_graph[pairs[0]].extend(pairs[1])
   return project_graph
graph = create_graph(['A', 'B', 'C', 'D', 'E', 'F'], [('A','D'), ('F', 'B'), ('B','D'), ('F','A'), ('D','C')])
# print(graph)
 
def get_projects_with_dependencies(graph):
   projects_with_depen = set()
   for project in graph:
       # addin values from dictionaty because values are dependednt of key
       projects_with_depen = projects_with_depen.union(set(graph[project]))
   
   return projects_with_depen
 
dependents = get_projects_with_dependencies(graph)
# print(dependents)
 
def get_projects_wo_dependencies(projects_with, graph):
   projects_wo_dependencies = set()
   for project in graph:
       if not project in projects_with:
           projects_wo_dependencies.add(project)
   return projects_wo_dependencies
notDependents = get_projects_wo_dependencies(dependents, graph)
# print(notDependents)
 
def find_build_order(projects, dependencies):
   build_order = []
   project_graph = create_graph(projects, dependencies)
   while project_graph:
       # print(project_graph)
       projects_with_depen = get_projects_with_dependencies(project_graph)
       projects_wo_depen = get_projects_wo_dependencies(projects_with_depen, project_graph)
       # print(projects_wo_depen)
       if len(projects_wo_depen) == 0 and project_graph:
           raise ValueError('There is a cycle in the build order')
       for independent_project in projects_wo_depen:
           build_order.append(independent_project)
           del project_graph[independent_project]
   return build_order
 
print(find_build_order(['A', 'B', 'C', 'D', 'E', 'F'], [('A','D'), ('F', 'B'), ('B','D'), ('F','A'), ('D','C')]))