# 1.1 - Retorne a quantidade de estudantes presentes para uma entrada específica;
# 1.2 - Retorne None se em permanence_period houver alguma entrada inválida;
# 1.3 - Retorne None se target_time recebe um valor vazio;
# 1.4 - A função deverá, por meio de análise empírica, se comportar (no avaliador remoto em sua Pull Request) como no máximo O(n), ou seja, com complexidade assintótica linear.

def study_schedule(permanence_period, target_time):
  students = 0
  
  for periodo in range(len(permanence_period)):
      if (
          not type(permanence_period[periodo][0]) is int
          or not type(permanence_period[periodo][1]) is int
      ):
          return None

      if not target_time:
          return None

      if target_time in range(
          permanence_period[periodo][0],
          permanence_period[periodo][1] + 1,
      ):
          students += 1
          
  return students   