// Generated from c:/Users/fette/Desktop/PROYECTO Sintaxis/MiLenguaje.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class MiLenguajeParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		OP_REL=25, CADENA=26, ID=27, NUMERO_REAL=28, NL=29, WS=30, COMENTARIO=31;
	public static final int
		RULE_programa = 0, RULE_declaracion_vars = 1, RULE_declaracion = 2, RULE_cuerpo_principal = 3, 
		RULE_sentencia = 4, RULE_asignacion = 5, RULE_lectura = 6, RULE_escritura = 7, 
		RULE_expr_escritura = 8, RULE_condicional = 9, RULE_repetitiva = 10, RULE_expr = 11, 
		RULE_condicion = 12;
	private static String[] makeRuleNames() {
		return new String[] {
			"programa", "declaracion_vars", "declaracion", "cuerpo_principal", "sentencia", 
			"asignacion", "lectura", "escritura", "expr_escritura", "condicional", 
			"repetitiva", "expr", "condicion"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'loadout'", "'{'", "'}'", "'real'", "':'", "','", "'spawn'", "'='", 
			"'loot'", "'('", "')'", "'drop'", "'peek'", "'fallback'", "'rush'", "'raiz'", 
			"'^'", "'*'", "'/'", "'+'", "'-'", "'no'", "'y'", "'o'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, "OP_REL", "CADENA", "ID", "NUMERO_REAL", "NL", "WS", "COMENTARIO"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "MiLenguaje.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public MiLenguajeParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramaContext extends ParserRuleContext {
		public Declaracion_varsContext declaracion_vars() {
			return getRuleContext(Declaracion_varsContext.class,0);
		}
		public Cuerpo_principalContext cuerpo_principal() {
			return getRuleContext(Cuerpo_principalContext.class,0);
		}
		public TerminalNode EOF() { return getToken(MiLenguajeParser.EOF, 0); }
		public ProgramaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_programa; }
	}

	public final ProgramaContext programa() throws RecognitionException {
		ProgramaContext _localctx = new ProgramaContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_programa);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(26);
			declaracion_vars();
			setState(27);
			cuerpo_principal();
			setState(28);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Declaracion_varsContext extends ParserRuleContext {
		public List<TerminalNode> NL() { return getTokens(MiLenguajeParser.NL); }
		public TerminalNode NL(int i) {
			return getToken(MiLenguajeParser.NL, i);
		}
		public List<DeclaracionContext> declaracion() {
			return getRuleContexts(DeclaracionContext.class);
		}
		public DeclaracionContext declaracion(int i) {
			return getRuleContext(DeclaracionContext.class,i);
		}
		public Declaracion_varsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaracion_vars; }
	}

	public final Declaracion_varsContext declaracion_vars() throws RecognitionException {
		Declaracion_varsContext _localctx = new Declaracion_varsContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_declaracion_vars);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(30);
			match(T__0);
			setState(31);
			match(T__1);
			setState(32);
			match(NL);
			setState(36);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__3) {
				{
				{
				setState(33);
				declaracion();
				}
				}
				setState(38);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(39);
			match(T__2);
			setState(41);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NL) {
				{
				setState(40);
				match(NL);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclaracionContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(MiLenguajeParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(MiLenguajeParser.ID, i);
		}
		public TerminalNode NL() { return getToken(MiLenguajeParser.NL, 0); }
		public DeclaracionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaracion; }
	}

	public final DeclaracionContext declaracion() throws RecognitionException {
		DeclaracionContext _localctx = new DeclaracionContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_declaracion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(43);
			match(T__3);
			setState(44);
			match(T__4);
			setState(45);
			match(ID);
			setState(50);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__5) {
				{
				{
				setState(46);
				match(T__5);
				setState(47);
				match(ID);
				}
				}
				setState(52);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(53);
			match(NL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Cuerpo_principalContext extends ParserRuleContext {
		public List<TerminalNode> NL() { return getTokens(MiLenguajeParser.NL); }
		public TerminalNode NL(int i) {
			return getToken(MiLenguajeParser.NL, i);
		}
		public List<SentenciaContext> sentencia() {
			return getRuleContexts(SentenciaContext.class);
		}
		public SentenciaContext sentencia(int i) {
			return getRuleContext(SentenciaContext.class,i);
		}
		public Cuerpo_principalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cuerpo_principal; }
	}

	public final Cuerpo_principalContext cuerpo_principal() throws RecognitionException {
		Cuerpo_principalContext _localctx = new Cuerpo_principalContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_cuerpo_principal);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(55);
			match(T__6);
			setState(56);
			match(T__1);
			setState(57);
			match(NL);
			setState(61);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 671134208L) != 0)) {
				{
				{
				setState(58);
				sentencia();
				}
				}
				setState(63);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(64);
			match(T__2);
			setState(66);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NL) {
				{
				setState(65);
				match(NL);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SentenciaContext extends ParserRuleContext {
		public AsignacionContext asignacion() {
			return getRuleContext(AsignacionContext.class,0);
		}
		public LecturaContext lectura() {
			return getRuleContext(LecturaContext.class,0);
		}
		public EscrituraContext escritura() {
			return getRuleContext(EscrituraContext.class,0);
		}
		public CondicionalContext condicional() {
			return getRuleContext(CondicionalContext.class,0);
		}
		public RepetitivaContext repetitiva() {
			return getRuleContext(RepetitivaContext.class,0);
		}
		public TerminalNode NL() { return getToken(MiLenguajeParser.NL, 0); }
		public SentenciaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sentencia; }
	}

	public final SentenciaContext sentencia() throws RecognitionException {
		SentenciaContext _localctx = new SentenciaContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_sentencia);
		try {
			setState(74);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(68);
				asignacion();
				}
				break;
			case T__8:
				enterOuterAlt(_localctx, 2);
				{
				setState(69);
				lectura();
				}
				break;
			case T__11:
				enterOuterAlt(_localctx, 3);
				{
				setState(70);
				escritura();
				}
				break;
			case T__12:
				enterOuterAlt(_localctx, 4);
				{
				setState(71);
				condicional();
				}
				break;
			case T__14:
				enterOuterAlt(_localctx, 5);
				{
				setState(72);
				repetitiva();
				}
				break;
			case NL:
				enterOuterAlt(_localctx, 6);
				{
				setState(73);
				match(NL);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AsignacionContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(MiLenguajeParser.ID, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode NL() { return getToken(MiLenguajeParser.NL, 0); }
		public AsignacionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_asignacion; }
	}

	public final AsignacionContext asignacion() throws RecognitionException {
		AsignacionContext _localctx = new AsignacionContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_asignacion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(76);
			match(ID);
			setState(77);
			match(T__7);
			setState(78);
			expr(0);
			setState(79);
			match(NL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LecturaContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(MiLenguajeParser.ID, 0); }
		public TerminalNode NL() { return getToken(MiLenguajeParser.NL, 0); }
		public LecturaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lectura; }
	}

	public final LecturaContext lectura() throws RecognitionException {
		LecturaContext _localctx = new LecturaContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_lectura);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(81);
			match(T__8);
			setState(82);
			match(T__9);
			setState(83);
			match(ID);
			setState(84);
			match(T__10);
			setState(85);
			match(NL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EscrituraContext extends ParserRuleContext {
		public List<Expr_escrituraContext> expr_escritura() {
			return getRuleContexts(Expr_escrituraContext.class);
		}
		public Expr_escrituraContext expr_escritura(int i) {
			return getRuleContext(Expr_escrituraContext.class,i);
		}
		public TerminalNode NL() { return getToken(MiLenguajeParser.NL, 0); }
		public EscrituraContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_escritura; }
	}

	public final EscrituraContext escritura() throws RecognitionException {
		EscrituraContext _localctx = new EscrituraContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_escritura);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(87);
			match(T__11);
			setState(88);
			match(T__9);
			setState(89);
			expr_escritura();
			setState(94);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__5) {
				{
				{
				setState(90);
				match(T__5);
				setState(91);
				expr_escritura();
				}
				}
				setState(96);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(97);
			match(T__10);
			setState(98);
			match(NL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expr_escrituraContext extends ParserRuleContext {
		public TerminalNode CADENA() { return getToken(MiLenguajeParser.CADENA, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Expr_escrituraContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr_escritura; }
	}

	public final Expr_escrituraContext expr_escritura() throws RecognitionException {
		Expr_escrituraContext _localctx = new Expr_escrituraContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_expr_escritura);
		try {
			setState(102);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CADENA:
				enterOuterAlt(_localctx, 1);
				{
				setState(100);
				match(CADENA);
				}
				break;
			case T__9:
			case T__15:
			case ID:
			case NUMERO_REAL:
				enterOuterAlt(_localctx, 2);
				{
				setState(101);
				expr(0);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CondicionalContext extends ParserRuleContext {
		public CondicionContext condicion() {
			return getRuleContext(CondicionContext.class,0);
		}
		public List<TerminalNode> NL() { return getTokens(MiLenguajeParser.NL); }
		public TerminalNode NL(int i) {
			return getToken(MiLenguajeParser.NL, i);
		}
		public List<SentenciaContext> sentencia() {
			return getRuleContexts(SentenciaContext.class);
		}
		public SentenciaContext sentencia(int i) {
			return getRuleContext(SentenciaContext.class,i);
		}
		public CondicionalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condicional; }
	}

	public final CondicionalContext condicional() throws RecognitionException {
		CondicionalContext _localctx = new CondicionalContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_condicional);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(104);
			match(T__12);
			setState(105);
			match(T__9);
			setState(106);
			condicion(0);
			setState(107);
			match(T__10);
			setState(108);
			match(T__1);
			setState(109);
			match(NL);
			setState(113);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 671134208L) != 0)) {
				{
				{
				setState(110);
				sentencia();
				}
				}
				setState(115);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(116);
			match(T__2);
			setState(127);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__13) {
				{
				setState(117);
				match(T__13);
				setState(118);
				match(T__1);
				setState(119);
				match(NL);
				setState(123);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 671134208L) != 0)) {
					{
					{
					setState(120);
					sentencia();
					}
					}
					setState(125);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(126);
				match(T__2);
				}
			}

			setState(130);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				{
				setState(129);
				match(NL);
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RepetitivaContext extends ParserRuleContext {
		public CondicionContext condicion() {
			return getRuleContext(CondicionContext.class,0);
		}
		public List<TerminalNode> NL() { return getTokens(MiLenguajeParser.NL); }
		public TerminalNode NL(int i) {
			return getToken(MiLenguajeParser.NL, i);
		}
		public List<SentenciaContext> sentencia() {
			return getRuleContexts(SentenciaContext.class);
		}
		public SentenciaContext sentencia(int i) {
			return getRuleContext(SentenciaContext.class,i);
		}
		public RepetitivaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_repetitiva; }
	}

	public final RepetitivaContext repetitiva() throws RecognitionException {
		RepetitivaContext _localctx = new RepetitivaContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_repetitiva);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(132);
			match(T__14);
			setState(133);
			match(T__9);
			setState(134);
			condicion(0);
			setState(135);
			match(T__10);
			setState(136);
			match(T__1);
			setState(137);
			match(NL);
			setState(141);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 671134208L) != 0)) {
				{
				{
				setState(138);
				sentencia();
				}
				}
				setState(143);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(144);
			match(T__2);
			setState(146);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				{
				setState(145);
				match(NL);
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprContext extends ParserRuleContext {
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	 
		public ExprContext() { }
		public void copyFrom(ExprContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ExprSumaRestaContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public ExprSumaRestaContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ExprPotenciaContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public ExprPotenciaContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ExprNumeroContext extends ExprContext {
		public TerminalNode NUMERO_REAL() { return getToken(MiLenguajeParser.NUMERO_REAL, 0); }
		public ExprNumeroContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ExprParensContext extends ExprContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ExprParensContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ExprMultDivContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public ExprMultDivContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ExprRaizContext extends ExprContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ExprRaizContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ExprIDContext extends ExprContext {
		public TerminalNode ID() { return getToken(MiLenguajeParser.ID, 0); }
		public ExprIDContext(ExprContext ctx) { copyFrom(ctx); }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 22;
		enterRecursionRule(_localctx, 22, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(160);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__9:
				{
				_localctx = new ExprParensContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(149);
				match(T__9);
				setState(150);
				expr(0);
				setState(151);
				match(T__10);
				}
				break;
			case T__15:
				{
				_localctx = new ExprRaizContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(153);
				match(T__15);
				setState(154);
				match(T__9);
				setState(155);
				expr(0);
				setState(156);
				match(T__10);
				}
				break;
			case ID:
				{
				_localctx = new ExprIDContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(158);
				match(ID);
				}
				break;
			case NUMERO_REAL:
				{
				_localctx = new ExprNumeroContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(159);
				match(NUMERO_REAL);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(173);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,16,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(171);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
					case 1:
						{
						_localctx = new ExprPotenciaContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(162);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(163);
						match(T__16);
						setState(164);
						expr(6);
						}
						break;
					case 2:
						{
						_localctx = new ExprMultDivContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(165);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(166);
						_la = _input.LA(1);
						if ( !(_la==T__17 || _la==T__18) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(167);
						expr(5);
						}
						break;
					case 3:
						{
						_localctx = new ExprSumaRestaContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(168);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(169);
						_la = _input.LA(1);
						if ( !(_la==T__19 || _la==T__20) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(170);
						expr(4);
						}
						break;
					}
					} 
				}
				setState(175);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,16,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CondicionContext extends ParserRuleContext {
		public CondicionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condicion; }
	 
		public CondicionContext() { }
		public void copyFrom(CondicionContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class CondOrContext extends CondicionContext {
		public List<CondicionContext> condicion() {
			return getRuleContexts(CondicionContext.class);
		}
		public CondicionContext condicion(int i) {
			return getRuleContext(CondicionContext.class,i);
		}
		public CondOrContext(CondicionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class CondAndContext extends CondicionContext {
		public List<CondicionContext> condicion() {
			return getRuleContexts(CondicionContext.class);
		}
		public CondicionContext condicion(int i) {
			return getRuleContext(CondicionContext.class,i);
		}
		public CondAndContext(CondicionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class CondNegacionContext extends CondicionContext {
		public CondicionContext condicion() {
			return getRuleContext(CondicionContext.class,0);
		}
		public CondNegacionContext(CondicionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class CondRelacionalContext extends CondicionContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode OP_REL() { return getToken(MiLenguajeParser.OP_REL, 0); }
		public CondRelacionalContext(CondicionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class CondParensContext extends CondicionContext {
		public CondicionContext condicion() {
			return getRuleContext(CondicionContext.class,0);
		}
		public CondParensContext(CondicionContext ctx) { copyFrom(ctx); }
	}

	public final CondicionContext condicion() throws RecognitionException {
		return condicion(0);
	}

	private CondicionContext condicion(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		CondicionContext _localctx = new CondicionContext(_ctx, _parentState);
		CondicionContext _prevctx = _localctx;
		int _startState = 24;
		enterRecursionRule(_localctx, 24, RULE_condicion, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(187);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
			case 1:
				{
				_localctx = new CondParensContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(177);
				match(T__9);
				setState(178);
				condicion(0);
				setState(179);
				match(T__10);
				}
				break;
			case 2:
				{
				_localctx = new CondNegacionContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(181);
				match(T__21);
				setState(182);
				condicion(4);
				}
				break;
			case 3:
				{
				_localctx = new CondRelacionalContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(183);
				expr(0);
				setState(184);
				match(OP_REL);
				setState(185);
				expr(0);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(197);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,19,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(195);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
					case 1:
						{
						_localctx = new CondAndContext(new CondicionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_condicion);
						setState(189);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(190);
						match(T__22);
						setState(191);
						condicion(3);
						}
						break;
					case 2:
						{
						_localctx = new CondOrContext(new CondicionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_condicion);
						setState(192);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(193);
						match(T__23);
						setState(194);
						condicion(2);
						}
						break;
					}
					} 
				}
				setState(199);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,19,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 11:
			return expr_sempred((ExprContext)_localctx, predIndex);
		case 12:
			return condicion_sempred((CondicionContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 5);
		case 1:
			return precpred(_ctx, 4);
		case 2:
			return precpred(_ctx, 3);
		}
		return true;
	}
	private boolean condicion_sempred(CondicionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 3:
			return precpred(_ctx, 2);
		case 4:
			return precpred(_ctx, 1);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u001f\u00c9\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001"+
		"\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004"+
		"\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007"+
		"\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b"+
		"\u0002\f\u0007\f\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0005\u0001#\b\u0001\n\u0001"+
		"\f\u0001&\t\u0001\u0001\u0001\u0001\u0001\u0003\u0001*\b\u0001\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0005\u00021\b\u0002"+
		"\n\u0002\f\u00024\t\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0005\u0003<\b\u0003\n\u0003\f\u0003?\t\u0003"+
		"\u0001\u0003\u0001\u0003\u0003\u0003C\b\u0003\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u0004K\b\u0004"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0005\u0007]\b\u0007"+
		"\n\u0007\f\u0007`\t\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b"+
		"\u0001\b\u0003\bg\b\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t"+
		"\u0001\t\u0005\tp\b\t\n\t\f\ts\t\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001"+
		"\t\u0005\tz\b\t\n\t\f\t}\t\t\u0001\t\u0003\t\u0080\b\t\u0001\t\u0003\t"+
		"\u0083\b\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0005"+
		"\n\u008c\b\n\n\n\f\n\u008f\t\n\u0001\n\u0001\n\u0003\n\u0093\b\n\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0003"+
		"\u000b\u00a1\b\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0005\u000b\u00ac"+
		"\b\u000b\n\u000b\f\u000b\u00af\t\u000b\u0001\f\u0001\f\u0001\f\u0001\f"+
		"\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0003\f\u00bc"+
		"\b\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0005\f\u00c4\b\f"+
		"\n\f\f\f\u00c7\t\f\u0001\f\u0000\u0002\u0016\u0018\r\u0000\u0002\u0004"+
		"\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u0000\u0002\u0001\u0000"+
		"\u0012\u0013\u0001\u0000\u0014\u0015\u00d7\u0000\u001a\u0001\u0000\u0000"+
		"\u0000\u0002\u001e\u0001\u0000\u0000\u0000\u0004+\u0001\u0000\u0000\u0000"+
		"\u00067\u0001\u0000\u0000\u0000\bJ\u0001\u0000\u0000\u0000\nL\u0001\u0000"+
		"\u0000\u0000\fQ\u0001\u0000\u0000\u0000\u000eW\u0001\u0000\u0000\u0000"+
		"\u0010f\u0001\u0000\u0000\u0000\u0012h\u0001\u0000\u0000\u0000\u0014\u0084"+
		"\u0001\u0000\u0000\u0000\u0016\u00a0\u0001\u0000\u0000\u0000\u0018\u00bb"+
		"\u0001\u0000\u0000\u0000\u001a\u001b\u0003\u0002\u0001\u0000\u001b\u001c"+
		"\u0003\u0006\u0003\u0000\u001c\u001d\u0005\u0000\u0000\u0001\u001d\u0001"+
		"\u0001\u0000\u0000\u0000\u001e\u001f\u0005\u0001\u0000\u0000\u001f \u0005"+
		"\u0002\u0000\u0000 $\u0005\u001d\u0000\u0000!#\u0003\u0004\u0002\u0000"+
		"\"!\u0001\u0000\u0000\u0000#&\u0001\u0000\u0000\u0000$\"\u0001\u0000\u0000"+
		"\u0000$%\u0001\u0000\u0000\u0000%\'\u0001\u0000\u0000\u0000&$\u0001\u0000"+
		"\u0000\u0000\')\u0005\u0003\u0000\u0000(*\u0005\u001d\u0000\u0000)(\u0001"+
		"\u0000\u0000\u0000)*\u0001\u0000\u0000\u0000*\u0003\u0001\u0000\u0000"+
		"\u0000+,\u0005\u0004\u0000\u0000,-\u0005\u0005\u0000\u0000-2\u0005\u001b"+
		"\u0000\u0000./\u0005\u0006\u0000\u0000/1\u0005\u001b\u0000\u00000.\u0001"+
		"\u0000\u0000\u000014\u0001\u0000\u0000\u000020\u0001\u0000\u0000\u0000"+
		"23\u0001\u0000\u0000\u000035\u0001\u0000\u0000\u000042\u0001\u0000\u0000"+
		"\u000056\u0005\u001d\u0000\u00006\u0005\u0001\u0000\u0000\u000078\u0005"+
		"\u0007\u0000\u000089\u0005\u0002\u0000\u00009=\u0005\u001d\u0000\u0000"+
		":<\u0003\b\u0004\u0000;:\u0001\u0000\u0000\u0000<?\u0001\u0000\u0000\u0000"+
		"=;\u0001\u0000\u0000\u0000=>\u0001\u0000\u0000\u0000>@\u0001\u0000\u0000"+
		"\u0000?=\u0001\u0000\u0000\u0000@B\u0005\u0003\u0000\u0000AC\u0005\u001d"+
		"\u0000\u0000BA\u0001\u0000\u0000\u0000BC\u0001\u0000\u0000\u0000C\u0007"+
		"\u0001\u0000\u0000\u0000DK\u0003\n\u0005\u0000EK\u0003\f\u0006\u0000F"+
		"K\u0003\u000e\u0007\u0000GK\u0003\u0012\t\u0000HK\u0003\u0014\n\u0000"+
		"IK\u0005\u001d\u0000\u0000JD\u0001\u0000\u0000\u0000JE\u0001\u0000\u0000"+
		"\u0000JF\u0001\u0000\u0000\u0000JG\u0001\u0000\u0000\u0000JH\u0001\u0000"+
		"\u0000\u0000JI\u0001\u0000\u0000\u0000K\t\u0001\u0000\u0000\u0000LM\u0005"+
		"\u001b\u0000\u0000MN\u0005\b\u0000\u0000NO\u0003\u0016\u000b\u0000OP\u0005"+
		"\u001d\u0000\u0000P\u000b\u0001\u0000\u0000\u0000QR\u0005\t\u0000\u0000"+
		"RS\u0005\n\u0000\u0000ST\u0005\u001b\u0000\u0000TU\u0005\u000b\u0000\u0000"+
		"UV\u0005\u001d\u0000\u0000V\r\u0001\u0000\u0000\u0000WX\u0005\f\u0000"+
		"\u0000XY\u0005\n\u0000\u0000Y^\u0003\u0010\b\u0000Z[\u0005\u0006\u0000"+
		"\u0000[]\u0003\u0010\b\u0000\\Z\u0001\u0000\u0000\u0000]`\u0001\u0000"+
		"\u0000\u0000^\\\u0001\u0000\u0000\u0000^_\u0001\u0000\u0000\u0000_a\u0001"+
		"\u0000\u0000\u0000`^\u0001\u0000\u0000\u0000ab\u0005\u000b\u0000\u0000"+
		"bc\u0005\u001d\u0000\u0000c\u000f\u0001\u0000\u0000\u0000dg\u0005\u001a"+
		"\u0000\u0000eg\u0003\u0016\u000b\u0000fd\u0001\u0000\u0000\u0000fe\u0001"+
		"\u0000\u0000\u0000g\u0011\u0001\u0000\u0000\u0000hi\u0005\r\u0000\u0000"+
		"ij\u0005\n\u0000\u0000jk\u0003\u0018\f\u0000kl\u0005\u000b\u0000\u0000"+
		"lm\u0005\u0002\u0000\u0000mq\u0005\u001d\u0000\u0000np\u0003\b\u0004\u0000"+
		"on\u0001\u0000\u0000\u0000ps\u0001\u0000\u0000\u0000qo\u0001\u0000\u0000"+
		"\u0000qr\u0001\u0000\u0000\u0000rt\u0001\u0000\u0000\u0000sq\u0001\u0000"+
		"\u0000\u0000t\u007f\u0005\u0003\u0000\u0000uv\u0005\u000e\u0000\u0000"+
		"vw\u0005\u0002\u0000\u0000w{\u0005\u001d\u0000\u0000xz\u0003\b\u0004\u0000"+
		"yx\u0001\u0000\u0000\u0000z}\u0001\u0000\u0000\u0000{y\u0001\u0000\u0000"+
		"\u0000{|\u0001\u0000\u0000\u0000|~\u0001\u0000\u0000\u0000}{\u0001\u0000"+
		"\u0000\u0000~\u0080\u0005\u0003\u0000\u0000\u007fu\u0001\u0000\u0000\u0000"+
		"\u007f\u0080\u0001\u0000\u0000\u0000\u0080\u0082\u0001\u0000\u0000\u0000"+
		"\u0081\u0083\u0005\u001d\u0000\u0000\u0082\u0081\u0001\u0000\u0000\u0000"+
		"\u0082\u0083\u0001\u0000\u0000\u0000\u0083\u0013\u0001\u0000\u0000\u0000"+
		"\u0084\u0085\u0005\u000f\u0000\u0000\u0085\u0086\u0005\n\u0000\u0000\u0086"+
		"\u0087\u0003\u0018\f\u0000\u0087\u0088\u0005\u000b\u0000\u0000\u0088\u0089"+
		"\u0005\u0002\u0000\u0000\u0089\u008d\u0005\u001d\u0000\u0000\u008a\u008c"+
		"\u0003\b\u0004\u0000\u008b\u008a\u0001\u0000\u0000\u0000\u008c\u008f\u0001"+
		"\u0000\u0000\u0000\u008d\u008b\u0001\u0000\u0000\u0000\u008d\u008e\u0001"+
		"\u0000\u0000\u0000\u008e\u0090\u0001\u0000\u0000\u0000\u008f\u008d\u0001"+
		"\u0000\u0000\u0000\u0090\u0092\u0005\u0003\u0000\u0000\u0091\u0093\u0005"+
		"\u001d\u0000\u0000\u0092\u0091\u0001\u0000\u0000\u0000\u0092\u0093\u0001"+
		"\u0000\u0000\u0000\u0093\u0015\u0001\u0000\u0000\u0000\u0094\u0095\u0006"+
		"\u000b\uffff\uffff\u0000\u0095\u0096\u0005\n\u0000\u0000\u0096\u0097\u0003"+
		"\u0016\u000b\u0000\u0097\u0098\u0005\u000b\u0000\u0000\u0098\u00a1\u0001"+
		"\u0000\u0000\u0000\u0099\u009a\u0005\u0010\u0000\u0000\u009a\u009b\u0005"+
		"\n\u0000\u0000\u009b\u009c\u0003\u0016\u000b\u0000\u009c\u009d\u0005\u000b"+
		"\u0000\u0000\u009d\u00a1\u0001\u0000\u0000\u0000\u009e\u00a1\u0005\u001b"+
		"\u0000\u0000\u009f\u00a1\u0005\u001c\u0000\u0000\u00a0\u0094\u0001\u0000"+
		"\u0000\u0000\u00a0\u0099\u0001\u0000\u0000\u0000\u00a0\u009e\u0001\u0000"+
		"\u0000\u0000\u00a0\u009f\u0001\u0000\u0000\u0000\u00a1\u00ad\u0001\u0000"+
		"\u0000\u0000\u00a2\u00a3\n\u0005\u0000\u0000\u00a3\u00a4\u0005\u0011\u0000"+
		"\u0000\u00a4\u00ac\u0003\u0016\u000b\u0006\u00a5\u00a6\n\u0004\u0000\u0000"+
		"\u00a6\u00a7\u0007\u0000\u0000\u0000\u00a7\u00ac\u0003\u0016\u000b\u0005"+
		"\u00a8\u00a9\n\u0003\u0000\u0000\u00a9\u00aa\u0007\u0001\u0000\u0000\u00aa"+
		"\u00ac\u0003\u0016\u000b\u0004\u00ab\u00a2\u0001\u0000\u0000\u0000\u00ab"+
		"\u00a5\u0001\u0000\u0000\u0000\u00ab\u00a8\u0001\u0000\u0000\u0000\u00ac"+
		"\u00af\u0001\u0000\u0000\u0000\u00ad\u00ab\u0001\u0000\u0000\u0000\u00ad"+
		"\u00ae\u0001\u0000\u0000\u0000\u00ae\u0017\u0001\u0000\u0000\u0000\u00af"+
		"\u00ad\u0001\u0000\u0000\u0000\u00b0\u00b1\u0006\f\uffff\uffff\u0000\u00b1"+
		"\u00b2\u0005\n\u0000\u0000\u00b2\u00b3\u0003\u0018\f\u0000\u00b3\u00b4"+
		"\u0005\u000b\u0000\u0000\u00b4\u00bc\u0001\u0000\u0000\u0000\u00b5\u00b6"+
		"\u0005\u0016\u0000\u0000\u00b6\u00bc\u0003\u0018\f\u0004\u00b7\u00b8\u0003"+
		"\u0016\u000b\u0000\u00b8\u00b9\u0005\u0019\u0000\u0000\u00b9\u00ba\u0003"+
		"\u0016\u000b\u0000\u00ba\u00bc\u0001\u0000\u0000\u0000\u00bb\u00b0\u0001"+
		"\u0000\u0000\u0000\u00bb\u00b5\u0001\u0000\u0000\u0000\u00bb\u00b7\u0001"+
		"\u0000\u0000\u0000\u00bc\u00c5\u0001\u0000\u0000\u0000\u00bd\u00be\n\u0002"+
		"\u0000\u0000\u00be\u00bf\u0005\u0017\u0000\u0000\u00bf\u00c4\u0003\u0018"+
		"\f\u0003\u00c0\u00c1\n\u0001\u0000\u0000\u00c1\u00c2\u0005\u0018\u0000"+
		"\u0000\u00c2\u00c4\u0003\u0018\f\u0002\u00c3\u00bd\u0001\u0000\u0000\u0000"+
		"\u00c3\u00c0\u0001\u0000\u0000\u0000\u00c4\u00c7\u0001\u0000\u0000\u0000"+
		"\u00c5\u00c3\u0001\u0000\u0000\u0000\u00c5\u00c6\u0001\u0000\u0000\u0000"+
		"\u00c6\u0019\u0001\u0000\u0000\u0000\u00c7\u00c5\u0001\u0000\u0000\u0000"+
		"\u0014$)2=BJ^fq{\u007f\u0082\u008d\u0092\u00a0\u00ab\u00ad\u00bb\u00c3"+
		"\u00c5";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}