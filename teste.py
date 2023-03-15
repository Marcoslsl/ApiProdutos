from src.infra.db.repo import ProdutoRepo

repo = ProdutoRepo()
print(repo.remove(1))