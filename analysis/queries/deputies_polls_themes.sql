SELECT
  CONCAT('d_', vv.deputado_id) AS deputado_id,
  CONCAT('v_', vv.idVotacao) AS votacao_id,
  vv.voto
FROM votacoesVotos vv
WHERE vv.voto IN ('Sim', 'Não')
  AND vv.idVotacao IN (
    SELECT DISTINCT vo.idVotacao
    FROM votacoesObjetos vo
    JOIN proposicoesTemas pt ON vo.proposicao_id = pt.proposicao_id
    WHERE pt.codTema = ?
  )