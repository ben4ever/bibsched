@Tags(const ['aot'])
@TestOn('browser')

import 'dart:html';

import 'package:angular/angular.dart';
import 'package:angular_components/angular_components.dart';
import 'package:angular_test/angular_test.dart';
import 'package:pageloader/html.dart';
import 'package:test/test.dart';

import 'package:bibsched/src/dashboard_component.dart';
import 'dashboard_po.dart';

PageLoader Function(Element el, NgTestFixture<DashboardComponent> fixture)
    _getCreatePageLoaderFunc(Element el) {
  return (_, fixture) => new HtmlPageLoader(el, executeSyncedFn: (fn) async {
        await fn();
        return fixture.update();
      });
}

@AngularEntrypoint()
void main() {
  DashboardPO po;
  NgTestFixture<DashboardComponent> fixture;

  tearDown(disposeAnyRunningTest);

  setUp(() async {
    var parentDiv = new DivElement(),
        hostDiv = new DivElement(),
        overlayContDiv = new DivElement();
    parentDiv.children..add(hostDiv)..add(overlayContDiv);
    final testBed = new NgTestBed<DashboardComponent>(host: hostDiv)
        .setPageLoader(_getCreatePageLoaderFunc(parentDiv))
        .addProviders([
      materialProviders,
    ]);
    fixture = await testBed.create();
    po = await fixture.resolvePageObject(DashboardPO);
    await fixture.update();
  });

  test('check initial state', () async {});
}
