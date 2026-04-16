SELECT
  vo.proposicao_id,
  vv.deputado_id,
  vv.voto
FROM
  votacoesVotos vv
  JOIN votacoesObjetos vo ON vv.idVotacao = vo.idVotacao;