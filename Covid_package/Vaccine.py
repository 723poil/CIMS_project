
class Vaccin:
    def __init__ (self, Vaccine):
     self.name = Vaccine["name"]
     self.company = Vaccine["company"]
     self.required_inoculations = Vaccine["required_inoculations"] #필요 접종 횟수
     self.inoculation_gap = Vaccine["inoculation_gap"] # 접종 간격
     self.inoculation_capacity = Vaccine["inoculation_capacity"] #접종 용량
     self.preventive_effects = Vaccine["preventive_effects"] # 예방 효과
     self.inoculation_rate = Vaccine["inoculation_rate"] #접종률
     self.side_effect_ex = Vaccine["side_effect_ex"] # 부작용 사례
     self.how_apply = Vaccine["how_apply"] 
     self.inoculation_person_num = Vaccine["inoculation_person_num"] #접종자 수

     def set():
        pass
