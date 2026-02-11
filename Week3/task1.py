import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

#ctrl.Antecedent(np.arange((start), (stop), (increment)), 'x')
time = ctrl.Antecedent(np.arange(0, 12.25, 0.25), 'time')
complexity = ctrl.Antecedent(np.arange(0, 101, 1), 'complexity')
additional_study_hours = ctrl.Consequent(np.arange(0, 12.25, 0.25), 'additional_study_hours')

#fuzz.zmf(x.universe, (starts decreasing from 1), (reaches 0))
time['short'] = fuzz.zmf(time.universe, 1, 3)
time['medium'] = fuzz.trapmf(time.universe, [1.5, 4, 5, 7])
time['long'] = fuzz.smf(time.universe, 5.25, 7)

complexity['easy'] = fuzz.zmf(complexity.universe, 25, 40)
complexity['medium'] = fuzz.trapmf(complexity.universe, [30, 50, 60, 70])
complexity['hard'] = fuzz.smf(complexity.universe, 65, 75)

additional_study_hours['low'] = fuzz.zmf(additional_study_hours.universe, 1, 3)
additional_study_hours['medium'] = fuzz.trapmf(additional_study_hours.universe, [1.5, 4, 5, 7])
additional_study_hours['high'] = fuzz.smf(additional_study_hours.universe, 5.25, 7)

complexity.view()

rule1 = ctrl.Rule(time['short'] | complexity['hard'], additional_study_hours['high'])
rule2 = ctrl.Rule(complexity['medium'], additional_study_hours['medium'])
rule3 = ctrl.Rule(time['long'] & complexity['easy'], additional_study_hours['low'])

additional_study_hours_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
additional_study_hours_sim = ctrl.ControlSystemSimulation(additional_study_hours_ctrl)

additional_study_hours_sim.input['time'] = 4.5
additional_study_hours_sim.input['complexity'] = 65

additional_study_hours_sim.compute()

additional_study_hours.view(sim=additional_study_hours_sim)

print (additional_study_hours_sim.output['additional_study_hours'])