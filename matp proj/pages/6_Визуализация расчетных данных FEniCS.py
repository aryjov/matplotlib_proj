"""
FEniCS tutorial demo program: Poisson equation with Dirichlet conditions.
Test problem is chosen to give an exact solution at all nodes of the mesh.

  -Laplace(u) = f    in the unit square
            u = u_D  on the boundary

  u_D = 1 + x^2 + 2y^2
    f = -6
"""

from __future__ import print_function
from fenics import *
import matplotlib.pyplot as plt
import streamlit as st

"""
# Решение задачи дирихле для уравнения Пуассона
### Тестовая задача выбирается так, чтобы дать точное решение во всех узлах сетки.
"""
st.latex(r'''
\begin{equation*}
    \begin{cases}
      -{\Delta}u = -6,  \;\;\;\;\; x,y \in \Omega\\
      u|_{\delta\Omega} = 1 + x^2 + 2y^2,  \\
    \end{cases}\
\end{equation*}

    ''')

fig, ax = plt.subplots()

# Create mesh and define function space
mesh = UnitSquareMesh(8, 8)
V = FunctionSpace(mesh, 'P', 1)



# Define boundary condition
u_D = Expression('1 + x[0]*x[0] + 2*x[1]*x[1]', degree=2)

def boundary(x, on_boundary):
    return on_boundary

bc = DirichletBC(V, u_D, boundary)

# Define variational problem
u = TrialFunction(V)
v = TestFunction(V)
f = Constant(-6.0)
a = dot(grad(u), grad(v))*dx
L = f*v*dx

# Compute solution
u = Function(V)
solve(a == L, u, bc)

# Plot solution and mesh
plot(u)
plot(mesh)


# Save solution to file in VTK format
#vtkfile = File('poisson/solution.pvd')



#vtkfile << u    # idk why it here in the first place





# Compute error in L2 norm
error_L2 = errornorm(u_D, u, 'L2')

# Compute maximum error at vertices
vertex_values_u_D = u_D.compute_vertex_values(mesh)
vertex_values_u = u.compute_vertex_values(mesh)
import numpy as np
error_max = np.max(np.abs(vertex_values_u_D - vertex_values_u))

# Print errors
#print('error_L2  =', error_L2)
#print('error_max =', error_max)

# Hold plot
#fig, ax = plt.subplots()
st.pyplot(fig)
#plt.savefig('probl.png')
#plt.savefig('probl.pdf')
#st.pyplot(plt.plot)
#plt.show()

with st.expander("Код"):
    code = '''
    """
FEniCS tutorial demo program: Poisson equation with Dirichlet conditions.
Test problem is chosen to give an exact solution at all nodes of the mesh.

  -Laplace(u) = f    in the unit square
        u = u_D  on the boundary

  u_D = 1 + x^2 + 2y^2
    f = -6
"""
       from __future__ import print_function
from fenics import *
import matplotlib.pyplot as plt
import streamlit as st

fig, ax = plt.subplots()

# Create mesh and define function space
mesh = UnitSquareMesh(8, 8)
V = FunctionSpace(mesh, 'P', 1)

# Define boundary condition
u_D = Expression('1 + x[0]*x[0] + 2*x[1]*x[1]', degree=2)

def boundary(x, on_boundary):
    return on_boundary

bc = DirichletBC(V, u_D, boundary)

# Define variational problem
u = TrialFunction(V)
v = TestFunction(V)
f = Constant(-6.0)
a = dot(grad(u), grad(v))*dx
L = f*v*dx

# Compute solution
u = Function(V)
solve(a == L, u, bc)

# Plot solution and mesh
plot(u)
plot(mesh)

# Save solution to file in VTK format
#vtkfile = File('poisson/solution.pvd')
#vtkfile << u    

# Compute error in L2 norm
error_L2 = errornorm(u_D, u, 'L2')

# Compute maximum error at vertices
vertex_values_u_D = u_D.compute_vertex_values(mesh)
vertex_values_u = u.compute_vertex_values(mesh)
import numpy as np
error_max = np.max(np.abs(vertex_values_u_D - vertex_values_u))

# Print errors
#print('error_L2  =', error_L2)
#print('error_max =', error_max)

# Hold plot
st.pyplot(fig)

    '''
    st.code(code, language='python')
    

with st.expander("Пример"):

    mesh = UnitSquareMesh(8, 8)
    V = FunctionSpace(mesh, 'P', 1)

    u_D = Expression('1 + x[0]*x[0] + 2*x[1]*x[1]', degree=2)

    def boundary(x, on_boundary):
        return on_boundary

    bc = DirichletBC(V, u_D, boundary)

    # Define variational problem
    u = TrialFunction(V)
    v = TestFunction(V)
    f = Constant(-6.0)
    a = dot(grad(u), grad(v))*dx
    L = f*v*dx


    u = Function(V)
    solve(a == L, u, bc)

    fig1, ax1 = plt.subplots()
    plot(u)
    fig2, ax2 = plt.subplots()
    plot(mesh)
    st.pyplot(fig1)
    st.pyplot(fig2)
