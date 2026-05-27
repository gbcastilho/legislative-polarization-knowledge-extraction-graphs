SELECT pt.codTema, pt.tema, COUNT(DISTINCT vo.idVotacao) as total_votacoes
FROM votacoesObjetos vo
RIGHT JOIN proposicoesTemas pt ON vo.proposicao_id = pt.proposicao_id
GROUP BY pt.codTema, pt.tema
ORDER BY total_votacoes DESC