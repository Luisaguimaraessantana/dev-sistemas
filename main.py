from datetime import datetime
from app.database import engine, Base, SessionLocal
from app.crud import inserir_tutor, inserir_animal, inserir_atendimento

def main():
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    try:
        data_hoje = datetime.now().strftime("%d/%m/%Y")

        tutor1 = inserir_tutor(db, nome_completo="Luisa Santana", telefone="61981234567", email="lucas.santana@email.com")
        print(f"Tutor inserido: {tutor1.nome_completo} (id={tutor1.id})")

        tutor2 = inserir_tutor(db, nome_completo="Gustavo Santos", telefone="61987654321", email="gustavo.santos@email.com")
        print(f"Tutor inserido: {tutor2.nome_completo} (id={tutor2.id})")

        animal1 = inserir_animal(db, nome_animal="Thor", especie="cão", raca="Golden Retriever", peso_kg=32.0, tutor_id=tutor1.id)
        print(f"Animal inserido: {animal1.nome_animal} - {animal1.especie}")

        animal2 = inserir_animal(db, nome_animal="Luna", especie="gato", raca="Persa", peso_kg=3.8, tutor_id=tutor1.id)
        print(f"Animal inserido: {animal2.nome_animal} - {animal2.especie}")

        animal3 = inserir_animal(db, nome_animal="Mel", especie="cão", raca="Poodle", peso_kg=6.5, tutor_id=tutor2.id)
        print(f"Animal inserido: {animal3.nome_animal} - {animal3.especie}")

        atend1 = inserir_atendimento(db, data_atend=data_hoje, motivo="Exame de sangue preventivo", valor_cons=180.00, animal_id=animal1.id)
        print(f"Atendimento: {atend1.motivo} | R$ {atend1.valor_cons:.2f}")

        atend2 = inserir_atendimento(db, data_atend=data_hoje, motivo="Limpeza periodontal e check-up", valor_cons=210.00, animal_id=animal2.id)
        print(f"Atendimento: {atend2.motivo} | R$ {atend2.valor_cons:.2f}")

        atend3 = inserir_atendimento(db, data_atend=data_hoje, motivo="Aplicação de vacina Antirrábica", valor_cons=95.00, animal_id=animal3.id)
        print(f"Atendimento: {atend3.motivo} | R$ {atend3.valor_cons:.2f}")

    finally:
        db.close()

if __name__ == "__main__":
    main()