SELECT 
    pt.codTema, 
    pt.tema, 
    COUNT(DISTINCT vv.deputado_id) as total_deputados
FROM  proposicoesTemas pt
LEFT JOIN votacoesObjetos vo ON pt.proposicao_id = vo.proposicao_id
LEFT JOIN votacoesVotos vv ON vo.idVotacao = vv.idVotacao
AND vv.voto IN ('Sim', 'Não')
GROUP BY pt.codTema, pt.tema
ORDER BY total_deputados DESC