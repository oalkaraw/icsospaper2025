import numpy as np
import matplotlib.pyplot as plt
import scipy.io
from scipy import integrate
plt.close('all')

#%%



REF_FORCE_DISP = scipy.io.loadmat('X_Y_Core_Force')


Force_Ref= np.sum(REF_FORCE_DISP['Force_Ref'][:, 1::2], axis=1)
Force_x_core= np.sum(REF_FORCE_DISP['Force_X_core'][:, 1::2], axis=1)
Force_Y_core= np.sum(REF_FORCE_DISP['Force_Y_Core'][:, 1::2], axis=1)

U_Ref = REF_FORCE_DISP['U_Ref'][:,1]
U_x_core = REF_FORCE_DISP['U_x_core'][:,1]
U_y_core = REF_FORCE_DISP['U_y_core'][:,1]


BETWEEN_FORCE_DISP = scipy.io.loadmat('Between_Force_U')
Force_Between= np.sum(BETWEEN_FORCE_DISP['Force_between'][:, 1::2], axis=1)

U_between= BETWEEN_FORCE_DISP['U_between'][:,1]

WHOLE_FORCE_DISP = scipy.io.loadmat('Whole_force')

Force_whole = np.sum(WHOLE_FORCE_DISP['Whole_force'][:, 1::2], axis=1)

U_Whole = WHOLE_FORCE_DISP['Whole_disp'][:,1]

PER_X_CORE = scipy.io.loadmat('per_x_core')

per_x_core = PER_X_CORE['per_x_core']


PER_Y_CORE = scipy.io.loadmat('per_y_core')

per_y_core = PER_Y_CORE['per_y_core']


PER_REF = scipy.io.loadmat('per_ref')

per_ref = PER_REF['per_ref']



REF_ENERGY_PER = scipy.io.loadmat('Ref_Energy_Per')
per_ref_energy = REF_ENERGY_PER['Ref_Energy_Per']

NEW_REF = scipy.io.loadmat('new_ref')

new_ref =  NEW_REF['new_ref']


CONCRETE_FORCE_DISP = scipy.io.loadmat('Force_disp_Concrete')
Force_Concrete = CONCRETE_FORCE_DISP['Force_disp_Concrete'][:,1]
Disp_Concrete = CONCRETE_FORCE_DISP['Force_disp_Concrete'][:,0]


REAL_TEST = scipy.io.loadmat('Exp')
test_disp = REAL_TEST['phy_test'][:,0]
test_force = REAL_TEST['phy_test'][:,1]


#%% Forces Ref + X + Y

from matplotlib.ticker import MultipleLocator

plt.figure(1)

plt.plot(U_Ref[0:176], Force_Ref[0:176] / 1e3, marker='o', linewidth=2)
plt.plot(U_x_core[0:156], Force_x_core[0:156] / 1e3, marker='^', linewidth=2)
plt.plot(U_y_core[0:162], Force_Y_core[0:162] / 1e3, marker='p', linewidth=2)

plt.xlabel('Indenter displacement [m]', fontsize=15)
plt.ylabel('Reaction force [kN]', fontsize=15)
plt.legend(['Reference','X-core','Y-core'], framealpha=1, fontsize=15)

ax = plt.gca()  # get current axis

# Keep major ticks as they are (automatic)
# Add minor ticks for denser grid without changing labels
ax.xaxis.set_minor_locator(MultipleLocator(0.0075))  # adjust spacing as needed
# ax.yaxis.set_minor_locator(MultipleLocator(5))   # adjust spacing as needed

# Grid for both major and minor ticks
ax.grid(which='major', color='black', linewidth=0.8)
ax.grid(which='minor', color='gray', linestyle=':', linewidth=0.5)

plt.show()

#%% Forces with Exp 


plt.figure()

plt.plot(U_Ref[0:176], Force_Ref[0:176] / 1e3, linewidth=2)
plt.xlabel('Indenter displacement [m]', fontsize=15)
plt.ylabel('Reaction force [kN]', fontsize=15)
# plt.title('Raction Forces- Reference Structures Comparison', fontsize=15)
plt.show()


plt.plot(test_disp, test_force,linestyle=':',color='#1f77b4', linewidth=2)
plt.grid(True)



plt.legend(['Current study','Karlsson et al. (2009)'],framealpha=1, fontsize=15)


#%% Forces Novel Structures Only


plt.figure()
plt.plot(Disp_Concrete[0:124], Force_Concrete[0:124] / 1e3,marker='p',  linewidth=2)

plt.grid(True)
plt.ylabel('Reaction Force [kN]', fontsize=15)
plt.show()
plt.plot(U_between[0:160], Force_Between[0:160] / 1e3,marker='o',  linewidth=2)

plt.plot(U_Whole[0:160], Force_whole[0:160] / 1e3,marker='^',  linewidth=2)
plt.grid(True)
plt.xlabel('Indenter displacement [m]', fontsize=15)
plt.ylabel('Reaction Force [kN]', fontsize=15)
plt.show()


plt.legend(['Concrete-filled','TB-F','TB-F'],framealpha=1, fontsize=15)




#%% Energies Ref

REF_ENERGY = scipy.io.loadmat('Ref_energy')

Ref_damage = REF_ENERGY['Ref_damage'][:,1]
Ref_Friction = REF_ENERGY['Ref_Friction'][:,1]
Ref_Plastic = REF_ENERGY['Ref_Plastic'][:,1]
Ref_viscous = REF_ENERGY['Ref_viscous'][:,1]
Ref_elastic = REF_ENERGY['Ref_elastic'][:,1]

Total_Eenergy_Ref = Ref_damage + Ref_Friction + Ref_Plastic + Ref_viscous + Ref_elastic

fig, ax = plt.subplots(3, 2, figsize=(20, 18))
ax[0,0].plot(U_Ref[0:176], Ref_damage[0:176] / 1e3,linestyle=":", linewidth=2)
ax[0,0].grid(True)
ax[0,0].set_xlabel('Indenter displacement [m]', fontsize=15)
ax[0,0].set_ylabel('Energy [kJ]', fontsize=15)
plt.show()
ax[0,0].plot(U_Ref[0:176], Ref_Friction[0:176] / 1e3,marker="o", linewidth=2)
ax[0,0].plot(U_Ref[0:176], Ref_Plastic[0:176] / 1e3,linestyle="--", linewidth=2)
ax[0,0].plot(U_Ref[0:176], Ref_viscous[0:176] / 1e3,linestyle="-.", linewidth=2)
ax[0,0].plot(U_Ref[0:176], Ref_elastic[0:176] / 1e3,linestyle="-", linewidth=2)
ax[0,0].plot(U_Ref[0:176], Total_Eenergy_Ref[0:176] / 1e3,marker="x", linewidth=2)

ax[0,0].set_xlim(0,0.45)
ax[0,0].set_ylim(0,400)

ax[0,0].legend(['Damage','Friction','Plastic','Viscous','Elastic','Total'],fontsize=14,framealpha=1,loc="upper left")

ax[0,0].text(x=0.1,y=350,s="Reference structure", fontsize=14, fontweight='bold', color='black',
        bbox=dict(facecolor='white', alpha=1, edgecolor='black'))



#%% Energies X-core


X_ENERGY = scipy.io.loadmat('X_energy')

X_damage = X_ENERGY['X_Damage'][:,1]
X_friction = X_ENERGY['X_friction'][:,1]
X_plastic = X_ENERGY['X_Plastic'][:,1]
X_viscous = X_ENERGY['X_Viscous'][:,1]
X_elastic = X_ENERGY['X_Elastic'][:,1]

Total_Eenergy_X = X_damage + X_friction + X_plastic + X_viscous + X_elastic

ax[0,1].plot(U_x_core[0:156], X_damage[0:156] / 1e3,linestyle=":", linewidth=2)
ax[0,1].grid(True)
ax[0,1].set_xlabel('Indenter displacement [m]', fontsize=15)
ax[0,1].set_ylabel('Energy [kJ]', fontsize=15)
plt.show()
ax[0,1].plot(U_x_core[0:156], X_friction[0:156] / 1e3,marker="o", linewidth=2)
ax[0,1].plot(U_x_core[0:156], X_plastic[0:156] / 1e3,linestyle="--", linewidth=2)
ax[0,1].plot(U_x_core[0:156], X_viscous[0:156] / 1e3,linestyle="-.", linewidth=2)
ax[0,1].plot(U_x_core[0:156], X_elastic[0:156] / 1e3,linestyle="-", linewidth=2)
ax[0,1].plot(U_x_core[0:156], Total_Eenergy_X[0:156] / 1e3,marker="x", linewidth=2)

ax[0,1].set_xlim(0,0.45)
ax[0,1].set_ylim(0,400)

ax[0,1].legend(['Damage','Friction','Plastic','Viscous','Elastic','Total'],fontsize=14,framealpha=1,loc="upper left")

ax[0,1].text(x=0.1,y=350,s="X-core", fontsize=14, fontweight='bold', color='black',
        bbox=dict(facecolor='white', alpha=1, edgecolor='black'))


#%% Energies Y-core
Y_ENERGY = scipy.io.loadmat('Y_energy')

Y_damage = Y_ENERGY['Y_Damage'][:,1]
Y_friction = Y_ENERGY['Y_Friction'][:,1]
Y_plastic = Y_ENERGY['Y_plastic'][:,1]
Y_viscous = Y_ENERGY['Y_viscous'][:,1]
Y_elastic = Y_ENERGY['Y_Strain'][:,1]

Total_Eenergy_Y = Y_damage + Y_friction + Y_plastic + Y_viscous + Y_elastic

ax[1,0].plot(U_y_core[0:162], Y_damage[0:162] / 1e3,linestyle=":", linewidth=2)
ax[1,0].grid(True)
ax[1,0].set_xlabel('Indenter displacement [m]', fontsize=15)
ax[1,0].set_ylabel('Energy [kJ]', fontsize=15)
plt.show()
ax[1,0].plot(U_y_core[0:162], Y_friction[0:162] / 1e3,marker="o", linewidth=2)
ax[1,0].plot(U_y_core[0:162], Y_plastic[0:162] / 1e3,linestyle="--", linewidth=2)
ax[1,0].plot(U_y_core[0:162], Y_viscous[0:162] / 1e3,linestyle="-.", linewidth=2)
ax[1,0].plot(U_y_core[0:162], Y_elastic[0:162] / 1e3,linestyle="-", linewidth=2)
ax[1,0].plot(U_y_core[0:162], Total_Eenergy_Y[0:162] / 1e3,marker="x", linewidth=2)

ax[1,0].set_xlim(0,0.45)
ax[1,0].set_ylim(0,400)
ax[1,0].legend(['Damage','Friction','Plastic','Viscous','Elastic','Total'],fontsize=14,framealpha=1,loc="upper left")
ax[1,0].text(x=0.1,y=350,s="Y-core", fontsize=14, fontweight='bold', color='black',
        bbox=dict(facecolor='white', alpha=1, edgecolor='black'))

#%% Energies 3rd Between


BETWEEN_ENERGY = scipy.io.loadmat('Energy_Between')

Between_Damage = BETWEEN_ENERGY['Between_Damage'][:,1]
Between_Friction = BETWEEN_ENERGY['Between_Friction'][:,1]
Between_Plastic = BETWEEN_ENERGY['Between_Plastic'][:,1]
Between_viscous = BETWEEN_ENERGY['Between_viscous'][:,1]
Between_elastic = BETWEEN_ENERGY['Between_elastic'][:,1]

Total_Eenergy_Between = Between_Damage + Between_Friction + Between_Plastic + Between_viscous + Between_elastic

ax[1,1].plot(U_between[0:160], Between_Damage[0:160] / 1e3,linestyle=":", linewidth=2)
ax[1,1].grid(True)
ax[1,1].set_xlabel('Indenter displacement [m]', fontsize=15)
ax[1,1].set_ylabel('Energy [kJ]', fontsize=15)
plt.show()
ax[1,1].plot(U_between[0:160], Between_Friction[0:160] / 1e3,marker="o", linewidth=2)
ax[1,1].plot(U_between[0:160], Between_Plastic[0:160] / 1e3,linestyle="--", linewidth=2)
ax[1,1].plot(U_between[0:160], Between_viscous[0:160] / 1e3,linestyle="-.", linewidth=2)
ax[1,1].plot(U_between[0:160], Between_elastic[0:160] / 1e3,linestyle="-", linewidth=2)
ax[1,1].plot(U_between[0:160], Total_Eenergy_Between[0:160] / 1e3,marker="x", linewidth=2)

ax[1,1].set_xlim(0,0.45)
ax[1,1].set_ylim(0,400)
ax[1,1].legend(['Damage','Friction','Plastic','Viscous','Elastic','Total'],fontsize=14,framealpha=1,loc="best")
ax[1,1].text(x=0.1,y=350,s="TB-BW", fontsize=14, fontweight='bold', color='black',
        bbox=dict(facecolor='white', alpha=1, edgecolor='black'))
 
#%% Energies 3rd Whole 

WHOLE_ENERGY = scipy.io.loadmat('Whole_Energy')

Whole_damage = WHOLE_ENERGY['Whole_damage'][:,1]
Whole_Friction = WHOLE_ENERGY['Whole_Friction'][:,1]
Whole_plastic = WHOLE_ENERGY['Whole_plastic'][:,1]
Whole_viscous = WHOLE_ENERGY['Whole_viscous'][:,1]
Whole_elastic = WHOLE_ENERGY['Whole_elastic'][:,1]

Total_Eenergy_Whole = Whole_damage + Whole_Friction + Whole_plastic + Whole_viscous + Whole_elastic

ax[2,0].plot(U_Whole[0:160], Whole_damage[0:160] / 1e3,linestyle=":", linewidth=2)
ax[2,0].grid(True)
ax[2,0].set_xlabel('Indenter displacement [m]', fontsize=15)
ax[2,0].set_ylabel('Energy [kJ]', fontsize=15)
plt.show()
ax[2,0].plot(U_Whole[0:160], Whole_Friction[0:160] / 1e3,marker="o", linewidth=2)
ax[2,0].plot(U_Whole[0:160], Whole_plastic[0:160] / 1e3,linestyle="--", linewidth=2)
ax[2,0].plot(U_Whole[0:160], Whole_viscous[0:160] / 1e3,linestyle="-.", linewidth=2)
ax[2,0].plot(U_Whole[0:160], Whole_elastic[0:160] / 1e3,linestyle="-", linewidth=2)
ax[2,0].plot(U_Whole[0:160], Total_Eenergy_Whole[0:160] / 1e3,marker="x", linewidth=2)
ax[2,0].set_xlim(0,0.45)
ax[2,0].set_ylim(0,400)


ax[2,0].legend(['Damage','Friction','Plastic','Viscous','Elastic','Total'],fontsize=14,framealpha=1,loc="upper left")
ax[2,0].text(x=0.1,y=350,s="TB-F", fontsize=14, fontweight='bold', color='black',
        bbox=dict(facecolor='white', alpha=1, edgecolor='black'))




#%% All Total Energies Reference strucutres





plt.figure()
plt.plot(U_Ref[0:176], Total_Eenergy_Ref[0:176]/ 1e3, linewidth=2)
plt.grid(True)
plt.xlabel('Indenter displacement [m]', fontsize=15)
plt.ylabel('Energy [kJ]', fontsize=15)
plt.plot(U_x_core[0:156], Total_Eenergy_X[0:156]/ 1e3,  linestyle=':',linewidth=2)
plt.plot(U_y_core[0:162], Total_Eenergy_Y[0:162] / 1e3, linestyle='--',linewidth=2)

plt.show()

plt.legend(['Reference','X-core','Y-core'],framealpha=1, fontsize=15)





#%% Energies Concrete

# energy_ref_abs = integrate.cumtrapz( new_ref[:,0], new_ref[:,1],initial=0)

new_ref_energy = scipy.io.loadmat('new_ref_energy')

new_ref_energy_new = new_ref_energy['new_ref_energy']


per_energy_x = scipy.io.loadmat('per_energy_x')

per_energy_x_new = per_energy_x['per_energy_x']


phy_eneg = scipy.io.loadmat('phy_eneg')

phy_eneg = phy_eneg['phy_eneg']

plt.figure()
plt.plot(U_Ref[0:176], Total_Eenergy_Ref[0:176] / 1e3, linewidth=2)
plt.grid(True)
plt.xlabel('Indenter displacement [m]', fontsize=15)
plt.ylabel('Energy [kJ]', fontsize=15)
# plt.title('Energy - Reference Structures Comparison', fontsize=15)
# plt.plot(U_x_core[0:153], Total_Eenergy_X[0:153] / 1e3, linewidth=2)
# plt.plot(U_y_core[0:154], Total_Eenergy_Y[0:154] / 1e3, linewidth=2)

plt.plot(test_disp, phy_eneg,linestyle=':',color='#1f77b4', linewidth=2)
# plt.plot(per_energy_x_new[:,0], per_energy_x_new[:,1],linestyle=':',color='#ff7f0e', linewidth=2)
plt.grid(True)

plt.legend(['Current study','Karlsson et al. (2009)'],framealpha=1, fontsize=15)

plt.show()







CONCRETE_ENERGY = scipy.io.loadmat('Concrete_Energies')

Concrete_damage = CONCRETE_ENERGY['Concrete_Damage'][:,1]
Concrete_Friction = CONCRETE_ENERGY['Concrete_Friction'][:,1]
Concrete_plastic = CONCRETE_ENERGY['Concrete_Plastic'][:,1]
Concrete_viscous = CONCRETE_ENERGY['Concrete_Viscous'][:,1]
Concrete_elastic = CONCRETE_ENERGY['Concrete_Elastic'][:,1]

Total_Eenergy_Concrete = Concrete_damage + Concrete_Friction + Concrete_plastic + Concrete_viscous + Concrete_elastic

ax[2,1].plot(Disp_Concrete[0:124], Concrete_damage[0:124] / 1e3,linestyle=":", linewidth=2)
ax[2,1].grid(True)
ax[2,1].set_xlabel('Indenter displacement [m]', fontsize=15)
ax[2,1].set_ylabel('Energy [kJ]', fontsize=15)
plt.show()
ax[2,1].plot(Disp_Concrete[0:124], Concrete_Friction[0:124] / 1e3,marker="o", linewidth=2)
ax[2,1].plot(Disp_Concrete[0:124], Concrete_plastic[0:124] / 1e3,linestyle="--", linewidth=2)
ax[2,1].plot(Disp_Concrete[0:124], Concrete_viscous[0:124] / 1e3,linestyle="-.", linewidth=2)
ax[2,1].plot(Disp_Concrete[0:124], Concrete_elastic[0:124] / 1e3,linestyle="-", linewidth=2)
ax[2,1].plot(Disp_Concrete[0:124], Total_Eenergy_Concrete[0:124] / 1e3,marker="x", linewidth=2)
ax[2,1].set_xlim(0,0.45)
ax[2,1].set_ylim(0,400)


ax[2,1].legend(['Damage','Friction','Plastic','Viscous','Elastic','Total'],fontsize=14,framealpha=1,loc="upper left")
ax[2,1].text(x=0.1,y=350,s="Concrete-filled reference structure", fontsize=14, fontweight='bold', color='black',
        bbox=dict(facecolor='white', alpha=1, edgecolor='black'))



#%% FORCES ALL


plt.figure()
plt.plot(U_Ref[0:176], Force_Ref[0:176] / 1e3, marker='o', linewidth=2)
plt.grid(True)
plt.xlabel('Indenter displacement [m]', fontsize=15)
plt.ylabel('Reaction force [kN]',  fontsize=15)
plt.show()

plt.plot(U_x_core[0:156], Force_x_core[0:156] / 1e3, linestyle='-', linewidth=2)

plt.plot(U_y_core[0:162], Force_Y_core[0:162] / 1e3, marker='^', linewidth=2)

plt.plot(U_between[0:160], Force_Between[0:160] / 1e3, linestyle='--', linewidth=2)

plt.plot(U_Whole[0:160], Force_whole[0:160] / 1e3, linestyle=':', linewidth=2)

plt.plot(Disp_Concrete[0:124], Force_Concrete[0:124] / 1e3, marker='x', linewidth=2)
ax = plt.gca()  # get current axis

# Keep major ticks as they are (automatic)
# Add minor ticks for denser grid without changing labels
ax.xaxis.set_minor_locator(MultipleLocator(0.0075))  # adjust spacing as needed
# ax.yaxis.set_minor_locator(MultipleLocator(5))   # adjust spacing as needed
# Grid for both major and minor ticks
ax.grid(which='major', color='black', linewidth=0.8)
ax.grid(which='minor', color='gray', linestyle=':', linewidth=0.5)

plt.legend(['Reference','X-core','Y-core','TB-BW','TB-F','Concrete-filled'],framealpha=1,fontsize=15)


#%% ENERGIES ALL


plt.figure()
plt.plot(U_Ref[0:176], Total_Eenergy_Ref[0:176] / 1e3, marker='o', linewidth=2)
plt.grid(True)
plt.xlabel('Indenter displacement [m]', fontsize=15)
plt.ylabel('Energy [kJ]',  fontsize=15)
plt.show()

plt.plot(U_x_core[0:156], Total_Eenergy_X[0:156] / 1e3, linestyle='-', linewidth=2)

plt.plot(U_y_core[0:162], Total_Eenergy_Y[0:162] / 1e3, linestyle='--', linewidth=2)

plt.plot(U_between[0:160], Total_Eenergy_Between[0:160] / 1e3, marker='o', linewidth=2)

plt.plot(U_Whole[0:160], Total_Eenergy_Whole[0:160] / 1e3, linestyle=':', linewidth=2)

plt.plot(Disp_Concrete[0:124], Total_Eenergy_Concrete[0:124] / 1e3, marker='x', linewidth=2)


plt.legend(['Reference','X-core','Y-core','TB-BW','TB-F','Concrete-filled'],framealpha=1,fontsize=15)


Ref_mass = 177.18

X_mass = 217.01
Y_mass = 167.17
Third2_mass = 355.92
Third1_mass = 282.64
Concrete_mass = 775.60



SEA_Ref_1 = (Total_Eenergy_Ref[176]/1e3)/ (Ref_mass)
SEA_X_1 = (Total_Eenergy_X[156]/1e3)/ (X_mass)
SEA_Y_1 = (Total_Eenergy_Y[162]/1e3)/ (Y_mass)
SEA_Third1_1 = (Total_Eenergy_Between[160]/1e3)/ (Third1_mass)
SEA_Third2_1 = (Total_Eenergy_Whole[160]/1e3)/ (Third2_mass)
SEA_Concrete_1 = (Total_Eenergy_Concrete[124]/1e3) / (Concrete_mass)


SEA_Ref = (SEA_Ref_1/ U_Ref[176])
SEA_X = (SEA_X_1/ U_x_core[156])
SEA_Y = (SEA_Y_1/ U_y_core[162])
SEA_Third1 = (SEA_Third1_1/ U_between[160])
SEA_Third2 = (SEA_Third2_1/ U_Whole[160])
SEA_Concrete = (SEA_Concrete_1/ Disp_Concrete[124])






