@Tags(const ['aot'])
@TestOn('browser')

import 'package:angular/angular.dart';
import 'package:test/test.dart';

import 'dashboard.dart' as dashboard;

@AngularEntrypoint()
void main() {
  group('dashboard:', dashboard.main);
}
